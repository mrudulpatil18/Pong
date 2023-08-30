import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((700,600))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

background_surface = pygame.image.load('./graphics/background.jpeg').convert_alpha()

slider1_rect = pygame.Rect((20,20) ,(10,75))
slider2_rect = pygame.Rect((20,20) ,(10,75))

slider1_rect.midleft = (40, 300)
slider2_rect.midright = (660, 300)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface, pygame.Rect(0,0,700,600))

    pygame.draw.rect(surface=screen, rect=slider1_rect, color='white')
    pygame.draw.rect(surface=screen, rect=slider2_rect, color='white')


    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        slider2_rect.y += 10
    if keys[pygame.K_UP]:
        slider2_rect.y -= 10
    if keys[pygame.K_s]:
        slider1_rect.y += 10
    if keys[pygame.K_w]:
        slider1_rect.y -= 10


    pygame.display.update()
    clock.tick(100)