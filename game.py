import sys, pygame
from pygame.locals import * 

# initializing pygame
pygame.init()

# pygame window design
background_color = (234, 212, 252)
screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption('Mushroom Mage')
screen.fill(background_color)
pygame.display.flip()

# var to keep the main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = False

        elif event.type == pygame.QUIT:
            running = False

