import pygame
import math

from surface import Surface

class Laser(Surface):
    def __init__(self, display, position, direction, arrow,sound):
        super().__init__(display, position, arrow.get_width(),height = arrow.get_height())
        # pygame.draw.circle(self.original_surface, (255, 255, 255), (4, 4), 4, width=2)
        self.original_surface.blit(arrow,(0,0))
        self.update_surface()

        self.original_surface = pygame.transform.rotate(self.original_surface, -math.degrees(direction) + 90)
        self.update_surface()

        self.direction = direction
        self.speed = 8

        self.sound = sound

        self.collision_point = (0,0)

        self._hit = False
    
    def move(self):
        self.position.x += math.cos(self.direction) * self.speed
        self.position.y += math.sin(self.direction) * self.speed

    def update(self,walls,enemies):
        self.move()
        self._hit = False

        self.walls_testing(walls)
        self.enemies_testing(enemies)

    def enemies_testing(self,enemies):
        for Type in list(enemies.keys()):
            for enem in enemies[Type]:
                if self.ray(enem):
                    if self.sound != None :self.sound.play()
                    self._hit = True

    def walls_testing(self,walls):
        for wall in walls:
            if self.ray(wall):
                if self.sound != None :self.sound.play()
                self._hit = True

    def ray(self,wall):

        x = (math.cos(self.direction)) * 30
        y = (math.sin(self.direction)) * 30

        width = self.get_width()

        while True:
            if x < width + width * 0.01 or y < width + width * 0.01:
                break 
            else:
                x /= 1.02
                y /= 1.02

        x = self.position.x + x
        y = self.position.y + y

        if wall.get_rect().collidepoint(x,y):
            self.collision_point = (x,y)
            return True
        return False

    @property
    def hit(self):
        return self._hit

    @property
    def collided(self):
        return self.collision_point