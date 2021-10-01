import pygame
import math

from surface import Surface
from laser import Laser

class Player(Surface):
    def __init__(self, display, position,Cavemen,Bow,sound):
        super().__init__(display, position, (Cavemen["caveman up"].get_width()))

        self.Cavemen = Cavemen
        self.original_surface.blit(Cavemen["caveman up"],(0,0))
        w = self.get_width()
        # pygame.draw.polygon(self.original_surface,(0,0,222),((0,0),(w,0),(w,w),(0,w)),1)
        self.update_surface()

        self.velocity = pygame.Vector2(0, 0)
        self.speed = 0.3
        self.direction = 0
    
        self.lasers = []

        self.blocked_key = []

        self.controlled = True

        self.sound = sound

        # draw bow
        self.Bow = Surface(self.surface,self.position,Bow[0].get_width())

        self.Bow.position.xy = (self.get_width() * 3 / 4 ,0)
        self.Bow.original_surface.blit(Bow[0],(0,0))
        self.Bow.update_surface()

        self.original_surface.blit(self.Bow.surface,(self.get_half()[0] ,0))

        self.original_surface.blit(Cavemen["caveman up"],(0,0))

        self.update_surface()

        #setup arrow
        self.Arrow = Bow[1]
        self.arrow = Surface(self.surface,(0,0),self.Arrow.get_width(),height = self.Arrow.get_height())
        self.arrow.original_surface.blit(self.Arrow,(0,0))
        self.arrow.update_surface()
        self.arrow.position.xy = (self.get_width() * 3 / 4 ,0)

        self.mouse_pressed = False

        self.shoot = False

        self._collided = None

    def stop_velocity_x(self):
        self.velocity.x = 0
    def stop_velocity_y(self):
        self.velocity.y = 0

    def block_key(self,key):
        self.blocked_key.append(key)

    def clear_blocked_keys(self):
        self.blocked_key.clear()

    def collides(self,pos):
        return self.get_rect().collidepoint(pos[0],pos[1])

    def shoot(self):
        self.lasers.append(Laser(self.DISPLAY, self.position, self.direction))
    
    def rotate(self):
        mx, my = pygame.mouse.get_pos()
        self.direction = -math.degrees(math.atan2(my - self.position.y, mx - self.position.x))
        self.surface = pygame.transform.rotate(self.original_surface, self.direction - 90)

    def move(self):
        self.direction = -math.radians(self.direction)

        keys = pygame.key.get_pressed()
        self.sound[0].stop()
        if keys[pygame.K_w] and not pygame.K_w in self.blocked_key:
            self.velocity.x += math.cos(self.direction)
            self.velocity.y += math.sin(self.direction)
            self.sound[0].play()
        # elif keys[pygame.K_s] and not pygame.K_s in self.blocked_key:
        #     self.velocity.x += math.cos(self.direction + math.radians(180)) 
        #     self.velocity.y += math.sin(self.direction + math.radians(180))
        # if keys[pygame.K_a] and not pygame.K_a in self.blocked_key:
        #     self.velocity.x += math.cos(self.direction - math.radians(90))
        #     self.velocity.y += math.sin(self.direction - math.radians(90))
        # elif keys[pygame.K_d] and not pygame.K_d in self.blocked_key:
        #     self.velocity.x += math.cos(self.direction + math.radians(90))
        #     self.velocity.y += math.sin(self.direction + math.radians(90))

        self.velocity /= 1.1

        if self.velocity.x > -0.3 and self.velocity.x < 0.3:
            self.velocity.x = 0
        if self.velocity.y > -0.3 and self.velocity.y < 0.3:
            self.velocity.y = 0

        self.position += (self.velocity * self.speed)

    def ray(self,wall,add,key):

        x = (math.cos(self.direction) + add) * 30
        y = (math.sin(self.direction) + add) * 30

        width = self.get_width()
        
        while True:
            if x < width + width * 0.01 or y < width + width * 0.01:
                break 
            else:
                x /= 1.02
                y /= 1.02

        x = self.position.x + x
        y = self.position.y + y

        try:
            if wall.get_rect().collidepoint(x,y):
                self.block_key(key[0])

                keys = pygame.key.get_pressed()
                if not keys[key[1]] and not keys[key[2]] and not keys[key[3]]:
                    self.stop_velocity_x()
                    self.stop_velocity_y()
        except:
            pass

    def collision(self,walls):
        for wall in walls:
            wall = self.ray(wall,0,[pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d])

    def hold_arrow(self):

        if not self.mouse_pressed and pygame.mouse.get_pressed()[0]:
            self.mouse_pressed = True
            self.arrow.draw()

        if self.mouse_pressed and pygame.mouse.get_pressed()[0] and len(self.lasers) < 1 and self.shoot:
            self.sound[3].play()
            self.mouse_pressed = False
            self.shoot = False
            self.lasers.append(Laser(self.DISPLAY, (self.position.x ,self.position.y), self.direction,self.Arrow,self.sound[2]))
            self.update_surface()

        if not self.shoot and not pygame.mouse.get_pressed()[0]:
            self.shoot = True
    @property
    def cords(self):
        return self._collided

    def update(self,walls = [],enemies = {}):
        if self.controlled:
            cords = None

            self._collided = None
            for laser in self.lasers:
                laser.draw()
                laser.update(walls,enemies)
                if laser.hit:
                    self._collided = laser.collided
                    self.lasers.pop(self.lasers.index(laser))
                

            self.collision(walls)
            self.hold_arrow()

            self.rotate()
            self.move()

            self.clear_blocked_keys()

            return cords

        else:
            self.rotate()
