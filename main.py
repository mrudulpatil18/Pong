import pygame
from sys import exit
import math
from random import randint

def move_ball(ball_x, ball_y):
    ball_x += ball_speed * math.cos(ball_direction)
    ball_y += ball_speed * math.sin(ball_direction)
    ball_rect.center = (ball_x, ball_y)
    return ball_x, ball_y

def handle_collision():
    if ball_rect.colliderect(slider1_rect) or ball_rect.colliderect(slider2_rect):
        if ball_rect.left >= 38 :
            ball_rect.x = 40
            return math.pi - ball_direction + math.radians(randint(-20,20))
        if ball_rect.right <= 762:
            ball_rect.x = 760
            return math.pi - ball_direction + math.radians(randint(-20,20))
        else:
            return 2 * math.pi - ball_direction
    if ball_rect.y <= 20 or ball_rect.y >= 580:
        return 2 * math.pi - ball_direction
    else:
        return ball_direction


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

score = [0,0]

ball_x = 400
ball_y = 300
ball_speed = 5
# clockwise angle with top axis
ball_direction = math.radians(randint(-45,45))
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

    screen.blit(background_surface, pygame.Rect(0,0,700,600))
    border_rect = pygame.draw.rect(surface=screen, rect=pygame.Rect(40, 20, 720, 560), color='white', width=1)
    pygame.draw.rect(surface=screen, rect=ball_rect, border_radius=3, color='white')
    pygame.draw.rect(surface=screen, rect=slider1_rect, color='white')
    pygame.draw.rect(surface=screen, rect=slider2_rect, color='white')

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
    pygame.display.update()
    clock.tick(100)