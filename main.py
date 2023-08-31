import pygame
from sys import exit
import math
from random import randint

def displayScore():

    game_active = 0

    player1_surf = test_font.render(str(score[0]), False, 'white')
    player1_rect = player1_surf.get_rect(midleft = (10,40))
    player2_surf = test_font.render(str(score[1]), False, 'white')
    player2_rect = player2_surf.get_rect(midright=(790, 40))

    screen.blit(player1_surf, player1_rect)
    screen.blit(player2_surf, player2_rect)
    return game_active

def update_score(won):
    score[won] += 1


def move_ball(ball_x, ball_y):
    ball_x += ball_speed * math.cos(ball_direction)
    ball_y += ball_speed * math.sin(ball_direction)
    ball_rect.center = (ball_x, ball_y)
    return ball_x, ball_y


def handle_collision():
    if ball_rect.colliderect(slider1_rect) or ball_rect.colliderect(slider2_rect):
        if ball_rect.left <= 40:
            ball_rect.left = 41
            return math.pi - ball_direction + math.radians(randint(-20,20))
        if ball_rect.right >= 760:
            ball_rect.right = 759
            return math.pi - ball_direction + math.radians(randint(-20,20))
    if ball_rect.top <= 20:
        ball_rect.top = 20
        return 2 * math.pi - ball_direction
    if ball_rect.bottom >= 580:
        ball_rect.bottom = 20
        return 2 * math.pi - ball_direction
    else:
        return ball_direction


def generate_direction():
    if chance == 0:
        return math.radians(randint(-20, 20)), 1
    else:
        return math.radians(randint(-160, 160)), 0


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

test_font = pygame.font.Font('./font/Pixeltype.ttf', 40)

game_active = 1
score = [0,0]
chance = 0

ball_x = 400
ball_y = 300
ball_speed = 5
# clockwise angle with top axis
ball_direction, chance = generate_direction()
ball_rect = pygame.Rect(10,10,10,10)

background_surface = pygame.image.load('./graphics/background.jpg').convert_alpha()

slider1_rect = pygame.Rect((20,20) ,(10,75))
slider2_rect = pygame.Rect((20,20) ,(10,75))

slider1_rect.midleft = (40, 300)
slider2_rect.midright = (760, 300)

pygame.draw.rect(surface=screen, rect=ball_rect, border_radius=3, color='white')
ball_rect.center = (400, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if not game_active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_active = 1
                print(chance)
                ball_direction, chance = generate_direction()
                ball_speed = 5

    screen.blit(background_surface, pygame.Rect(0,0,700,600))
    border_rect = pygame.draw.rect(surface=screen, rect=pygame.Rect(50, 20, 700, 560), color=(64,64,64), width=1)
    pygame.draw.rect(surface=screen, rect=ball_rect, border_radius=3, color='white')
    pygame.draw.rect(surface=screen, rect=slider1_rect, color='white', border_radius=3)
    pygame.draw.rect(surface=screen, rect=slider2_rect, color='white', border_radius=3)

    displayScore()

    if game_active:
        ball_x, ball_y = move_ball(ball_x, ball_y)
        ball_direction = handle_collision()

        keys = pygame.key.get_pressed()

        # move sliders with keys
        if keys[pygame.K_DOWN]:
            slider2_rect.y += 5
        if keys[pygame.K_UP]:
            slider2_rect.y -= 5
        if keys[pygame.K_s]:
            slider1_rect.y += 5
        if keys[pygame.K_w]:
            slider1_rect.y -= 5

        # restrict slider within box
        if slider1_rect.bottom >= 580:
            slider1_rect.bottom = 580
        elif slider1_rect.top <= 20:
            slider1_rect.top = 20

        if slider2_rect.bottom >= 580:
            slider2_rect.bottom = 580
        elif slider2_rect.top <= 20:
            slider2_rect.top = 20

        ball_speed += 0.0001

        if ball_rect.left >= 760:
            ball_x = 400
            ball_y = 300
            ball_rect.center = (ball_x, ball_y)
            game_active = update_score(0)
        elif ball_rect.right <= 40:
            ball_x = 400
            ball_y = 300
            ball_rect.center = (ball_x, ball_y)
            game_active = update_score(1)
    else:
        press_surf = test_font.render("Press Enter To Continue", False, 'white')
        press_rect = press_surf.get_rect(center=(400, 200))


        screen.blit(press_surf, press_rect)


    pygame.display.update()
    clock.tick(100)