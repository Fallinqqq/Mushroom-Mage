import pygame
from pygame.locals import *

# pygame window design / import
background_color = (234, 212, 252)
screen = pygame.display.set_mode((900, 800))
pygame.display.set_caption('Mushroom Mage')
screen.fill(background_color)
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
