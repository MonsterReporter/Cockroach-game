import sys
import os
sys.path.append(os.path.join(os.getcwd(),"code"))

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

#setup the spirites/images/surfaces adujuster.
class adujuster():
    def __init__(self,size_x,size_y,full):
        self._size_x = size_x
        self._size_y = size_y
        self._full = full

    def get_size(self):
        return (self._size_x,self._size_y)
    def get_size_x(self):
        return self._size_x
    def get_size_y(self):
        return self._size_y
    def get_surface_size(self,size):
        #size is width, height
        return (int(30 / size[0] * 1920),int( 60 / size[1] * 1080))

<<<<<<< Updated upstream

# Set up the window.
with open("settings.txt","r") as file:
    file = list(file.read().split("\n"))

    size_x, size_y , full = 640, 480, False
    
    for i in file:
        if i.startswith("#"):
            file.pop(file.index(i))
        if i.startswith("FullScreen"):
            full = bool(int(i.split(":")[1]))
        if i.startswith("screenSize_x"):
            size_x = int(i.split(":")[1])
        if i.startswith("screenSize_y"):
            size_y = int(i.split(":")[1])

    size = (size_x,size_y)

    if full:
        screen = pygame.display.set_mode(size,FULLSCREEN)
    else:
        screen = pygame.display.set_mode(size)

Adujuster = adujuster(size_x,size_y,full)

# icon
# icon = pygame.image.load("none")
# pygame.display.set_icon(icon)

# title
pygame.display.set_caption("game")

#import textures
placeholder = pygame.image.load("textures/placeholder.png")
placeholder = pygame.transform.scale(placeholder,size)
placeholder2 = pygame.image.load("textures/placeholder2.png")
placeholder2 = pygame.transform.scale(placeholder2,Adujuster.get_surface_size((size_x,size_y)))

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
=======
if __name__ == "__main__":
    main()
def main():
    import pygame

    from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FRAMERATE
    from manager import Manager

    pygame.init()

    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    CLOCK = pygame.time.Clock()

    manager = Manager(SCREEN, CLOCK)

    while(1):
        manager.run()
        CLOCK.tick(FRAMERATE)

if __name__ == "__main__":
    main()
>>>>>>> Stashed changes
