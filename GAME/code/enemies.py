import pygame
import math

from surface import Surface

from laser import Laser

class enemy_manager():
    def __init__(self,display,Enemie1):
        self.DISPLAY = display
        self.Enemie1 = Enemie1
        self.DISPLAY_WIDTH = display.get_width()
        self.DISPLAY_HEIGHT = display.get_height()
        self.Enemies = {"cockroach":[]}

    def get_enemies(self,Type):
        output = []
        for enem in self.Enemies [Type]:
            output.append(enem)
        return output

    def get_enemies_all(self):
        return self.Enemies

    def clear(self):
        self.Enemies = {"cockroach":[]}

    def clear_type(self,Type):
        self.Enemies[Type].clear()

    def remove(self,pos):
        output = []
        for Type in list(self.Enemies.keys()):
            for enem in self.Enemies[Type]:

                if enem.get_rect().collidepoint(pos):
                    self.Enemies[Type].pop(self.Enemies[Type].index(enem))
                    # print("rm:",pos)
                    break

    def get_count(self):
        output = 0
        for Type in list(self.Enemies.keys()):
            output += len(self.Enemies[Type])
        return output

    def update(self,walls,player_pos):
        for Type in list(self.Enemies.keys()):
            for enem in self.Enemies[Type]:

                if enem.update(walls,player_pos):
                    self.Enemies[Type].pop(self.Enemies[Type].index(enem))

                enem.draw()

    def add_Enemie(self,display,Type,position,active):
        if Type == "cockroach":
            self.Enemies[Type].append(cockroach(display,position,self.Enemie1["cup"].get_size(),self.Enemie1,active))


class cockroach(Surface):
    def __init__(self,display,position,size,sprites,active):
        super().__init__(display, position, (size[0]),height = size[1])

        self.sprites = sprites
        self.original_surface.blit(self.sprites["cup"],(0,0))
        w = self.get_width()
        # pygame.draw.polygon(self.original_surface,(0,0,222),((0,0),(w,0),(w,w),(0,w)),1)
        self.update_surface()

        self.velocity = pygame.Vector2(0, 0)
        self.turn = pygame.Vector2(0,0)
        self.speed = 0.3
        self.direction = 0
    
        self.lasers = []

        self.blocked_key = []

        self.active = active

        self.collided = False

        self.sec = 0
        self.start_ticks=pygame.time.get_ticks()

    def rotate(self):
        if self.collided:
            mx = self.turn.x
            my = self.turn.y
            # print(self.direction)
            self.direction = -math.degrees(math.atan2(my - self.position.y, mx - self.position.x))
            self.surface = pygame.transform.rotate(self.original_surface, self.direction - 90)
            self.collided = False
            # print(self.direction)
            # print(self.position.xy, mx , my)

        else:
            self.surface = pygame.transform.rotate(self.original_surface, self.direction - 90)

    def move(self):
        direction = -math.radians(self.direction)

        keys = pygame.key.get_pressed()
        if not self.collided:
            self.velocity.x += math.cos(direction)
            self.velocity.y += math.sin(direction)

        self.velocity /= 1.1

        if self.velocity.x > -0.3 and self.velocity.x < 0.3:
            self.velocity.x = 0
        if self.velocity.y > -0.3 and self.velocity.y < 0.3:
            self.velocity.y = 0

        self.position += (self.velocity * self.speed)

    def ray(self,wall):

        x = (math.cos(self.direction)) * 30
        y = (math.sin(self.direction)) * 30

        width = self.get_width()
        
        while True:
            if x < width + width * 0.1 or y < width + width * 0.1:
                break 
            else:
                x /= 1.02
                y /= 1.02
        sx,sy = x,y
        x = self.position.x + x
        y = self.position.y + y

        try:
            if wall.get_rect().collidepoint(x,y):# and self.sec < (pygame.time.get_ticks()-self.start_ticks)/1000:
                self.collided = True
                # self.turn.x = self.position.x + (math.cos(self.direction) + math.radians(180))
                # self.turn.y = self.position.y + (math.sin(self.direction) + math.radians(180))
                self.turn.x = self.position.x + (sx * -1)
                self.turn.y = self.position.y + (sy * -1)

                # self.sec = 0.01
                # self.start_ticks=pygame.time.get_ticks()
                # print(self.turn.xy)

        except:
            pass

    def collision(self,walls):
        for wall in walls:
            wall = self.ray(wall)

    def player_shoot(self,player_pos):
        pass

    def update(self,walls,player_pos):
        if self.active:

            for laser in self.lasers:
                laser.draw()
                if laser.update(walls):
                    self.lasers.pop(self.lasers.index(laser))
                

            self.collision(walls)
            self.player_shoot(player_pos)

            self.rotate()
            self.move()

            if self.position.x > self.DISPLAY_WIDTH or self.position.y > self.DISPLAY_HEIGHT \
                or self.position.x < 0 or self.position.y < 0:
                # print("gone")
                return True

        else:
            self.rotate()

        return False
