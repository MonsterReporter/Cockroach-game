import pygame
import math

from surface import Surface

class Player(Surface):
    def __init__(self, display, position):
        super().__init__(display, position, (32))
        pygame.draw.polygon(self.original_surface, (255, 255, 255), ((16, 0), (32, 32), (16, 26), (0, 32)), width=2)
        self.update_surface()

        self.velocity = pygame.Vector2(0, 0)
        self.speed = 0.3
        self.direction = 0
    
    def rotate(self):
        mx, my = pygame.mouse.get_pos()
        self.direction = -math.degrees(math.atan2(my - self.position.y, mx - self.position.x))
        self.surface = pygame.transform.rotate(self.original_surface, self.direction - 90)

    def move(self):
        self.direction = -math.radians(self.direction)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.velocity.x += math.cos(self.direction)
            self.velocity.y += math.sin(self.direction)
        if keys[pygame.K_a]:
            self.velocity.x += math.cos(self.direction) - math.radians(90)
        elif keys[pygame.K_d]:
            self.velocity.x += math.cos(self.direction) + math.radians(90)

        self.velocity /= 1.02

        if self.velocity.x > -0.3 and self.velocity.x < 0.3:
            self.velocity.x = 0
        if self.velocity.y > -0.3 and self.velocity.y < 0.3:
            self.velocity.y = 0

        self.position += (self.velocity * self.speed)

    def update(self):
        self.rotate()
        self.move()
