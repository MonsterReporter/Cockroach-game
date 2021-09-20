import sys
import os
sys.path.append(os.path.dirname"/code")
import pygame
from pygame.locals import *
from pygame import mixer
from random import randint as rd
from player import player as P 

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

    size = (size_x,size_y)

    if full:
        screen = pygame.display.set_mode(size,FULLSCREEN)
    else:
        screen = pygame.display.set_mode(size)

# icon
# icon = pygame.image.load("none")
# pygame.display.set_icon(icon)

# title
pygame.display.set_caption("game")

#import textures
placeholder = pygame.image.load("textures/placeholder.png")
placeholder = pygame.transform.scale(placeholder,size)
placeholder2 = pygame.image.load("textures/placeholder2.png")
placeholder2 = pygame.transform.scale(placeholder2,(int(30 / size_x * 1920),int( 60 / size_y * 1080)))

#Sart stuff
P = P(100,100,placeholder2)
dt = 0
font = pygame.font.SysFont("Arial", 24)

running = True
while running:

    #exiting the game
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
    #floor
    screen.blit(placeholder,(0,0))

    #player
    screen = P.update(screen,dt,font)

    pygame.display.update()

    dt = fpsClock.tick(fps)

pygame.quit()
sys.exit()