import pygame
from pygame.locals import *

class wall_manager():
    def __init__(self,img):
        #the image is the type of the wall.
        self.img = img
        self.walls = []

    def add_wall(self,x,y,size):
        pass

class wall(pygame.Surface):
    def __init__(self ,w , h, img):
        pygame.Surface.__init__(self, size=(w, h))
        self.blit(img, (0 ,0)