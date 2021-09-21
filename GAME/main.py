<<<<<<< Updated upstream
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

#Sart stuff
font = pygame.font.SysFont("Arial", 24)



=======
>>>>>>> Stashed changes
def main():
    import sys
    import os
    sys.path.append(os.path.join(os.getcwd(),"code")) 
    
    import pygame

    # from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FRAMERATE
    from screen_ import *
    from manager import Manager

    pygame.init()

    SCREEN = set_up_scree()
    CLOCK = pygame.time.Clock()

    manager = Manager(SCREEN, CLOCK)

    while(1):
        manager.run()
        CLOCK.tick(60)

if __name__ == "__main__":
    main()