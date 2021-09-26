import pygame
import math

from surface import Surface
from laser import Laser

class Player(Surface):
    def __init__(self, display, position,Cavemen,Bow):
        super().__init__(display, position, (Cavemen["caveman up"].get_width()))

        self.Cavemen = Cavemen
        self.original_surface.blit(Cavemen["caveman up"],(0,0))
        w = self.get_width()
        pygame.draw.polygon(self.original_surface,(0,0,222),((0,0),(w,0),(w,w),(0,w)),1)
        self.update_surface()

        self.velocity = pygame.Vector2(0, 0)
        self.speed = 0.3
        self.direction = 0
    
        self.lasers = []

        self.blocked_key = []

        self.controlled = True

        self.Bow = Surface(self.DISPLAY,self.position)

    def stop_velocity_x(self):
        self.velocity.x = 0
    def stop_velocity_y(self):
        self.velocity.y = 0

    def block_key(self,key):
        self.blocked_key.append(key)

    def clear_blocked_keys(self):
        self.blocked_key.clear()

    def shoot(self):
        self.lasers.append(Laser(self.DISPLAY, self.position, self.direction))
    
    def rotate(self):
        mx, my = pygame.mouse.get_pos()
        self.direction = -math.degrees(math.atan2(my - self.position.y, mx - self.position.x))
        self.surface = pygame.transform.rotate(self.original_surface, self.direction - 90)

    def move(self):
        self.direction = -math.radians(self.direction)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and not pygame.K_w in self.blocked_key:
            self.velocity.x += math.cos(self.direction)
            self.velocity.y += math.sin(self.direction)
        elif keys[pygame.K_s] and not pygame.K_s in self.blocked_key:
            self.velocity.x += math.cos(self.direction + math.radians(180)) 
            self.velocity.y += math.sin(self.direction + math.radians(180))
        if keys[pygame.K_a] and not pygame.K_a in self.blocked_key:
            self.velocity.x += math.cos(self.direction - math.radians(90))
            self.velocity.y += math.sin(self.direction - math.radians(90))
        elif keys[pygame.K_d] and not pygame.K_d in self.blocked_key:
            self.velocity.x += math.cos(self.direction + math.radians(90))
            self.velocity.y += math.sin(self.direction + math.radians(90))


        self.velocity /= 1.02

        if self.velocity.x > -0.3 and self.velocity.x < 0.3:
            self.velocity.x = 0
        if self.velocity.y > -0.3 and self.velocity.y < 0.3:
            self.velocity.y = 0

        self.position += (self.velocity * self.speed)

    def update(self):
        if self.controlled:

            for laser in self.lasers:
                laser.update()
                laser.draw()

            self.rotate()
            self.move()

            self.clear_blocked_keys()

        else:
            self.rotate()
