import pygame
import math

from surface import Surface

class Laser(Surface):
    def __init__(self, display, position, direction):
        super().__init__(display, position, 8)
        pygame.draw.circle(self.original_surface, (255, 255, 255), (4, 4), 4, width=2)
        self.update_surface()

        self.direction = direction
        self.speed = 8
    
    def move(self):
        self.position.x += math.cos(self.direction) * self.speed
        self.position.y += math.sin(self.direction) * self.speed

    def update(self):
        self.move()