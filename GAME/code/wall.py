import pygame
from pygame.locals import *

class wall():
    class MyWindow(pygame.Surface):
        def __init__(self, Adujuster):
            pygame.Surface.__init__(self, size=(w, h))