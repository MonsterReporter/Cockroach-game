import sys
import pygame
from pygame.locals import *
from pygame import mixer
from random import randint as rd

# Initialise PyGame.
pygame.init()

# Set up the clock.
fps = 60.0
fpsClock = pygame.time.Clock()

# Set up the window.
with open("settings.txt","r") as file:
    file = list(file.read().split("\n"))

    size_x, size_y , full = 640, 480, False
    
    for i in file:
        if i.startswith("#"):
            file.pop(file.index(i))
        if i.startswith("full"):
            full = bool(int(i.split(":")[1]))
        if i.startswith("size_x"):
            size_x = int(i.split(":")[1])
        if i.startswith("size_y"):
            size_y = int(i.split(":")[1])

    if full:
        screen = pygame.display.set_mode((size_x, size_y),FULLSCREEN)
    else:
        screen = pygame.display.set_mode((size_x, size_y))

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

    #testing circle
    pygame.draw.circle(screen,(rd(90,120),255,255),(100,100),rd(10,100))

    pygame.display.update()

    dt = fpsClock.tick(fps)

pygame.quit()
sys.exit()