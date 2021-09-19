import pygame
from pygame.locals import *
class player():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.v = 0.5

        self.vel = [0,0]

    def update(self,screen,dt):
        screen.blit(self.img,(self.x,self.y))

        keys = pygame.key.get_pressed()

        if keys[K_w]:
            self.y -= self.v * dt

        if keys[K_s]:
            self.y += self.v * dt

        if keys[K_d]:
            self.x += self.v * dt

        if keys[K_a]:
            self.x -= self.v * dt
 

        return screen