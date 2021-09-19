import sys
import pygame
from pygame.locals import *
from pygame import mixer
from random import randint

# Initialise PyGame.
pygame.init()

# Set up the clock.
fps = 60.0
fpsClock = pygame.time.Clock()

# Set up the window.
width, height = int(1920), int(1080)
screen = pygame.display.set_mode((width, height))

# icon
# icon = pygame.image.load("none")
# pygame.display.set_icon(icon)

# title
pygame.display.set_caption("game")


running = True

while running:

    #exiting the game
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    pygame.display.update()

    dt = fpsClock.tick(fps)

pygame.quit()
sys.exit()