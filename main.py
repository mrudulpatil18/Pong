import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

slider1_rect = pygame.rect.Rect(10,10,)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(100)