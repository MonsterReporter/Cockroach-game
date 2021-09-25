import pygame
from pygame.locals import *

class enemy_manager(self):
    def __init__(self,display):
        self.DISPLAY = display
        self.DISPLAY_WIDTH = display.get_width()
        self.DISPLAY_HEIGHT = display.get_height()