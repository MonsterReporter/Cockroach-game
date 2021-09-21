import pygame
from pygame.locals import *

class wall_manager():
    def __init__(self,imgs):
        #the image is a dict the all types of the walls.
        self.imgs = imgs
        self.walls = []

    def add_wall(self,x,y,img_name):
        size = self.imgs[img_name].size
        img = self.imgs[img_name]
        self.walls.append(wall((x,y),size,img))

    def update(self,player):
        for wall in self.walls:
            player = wall.update(player)



class wall(pygame.Surface):
    def __init__(self ,(size), img):
        pygame.Surface.__init__(self, size=(size))
        self.blit(img, (0 ,0)