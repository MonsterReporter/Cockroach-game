import pygame

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

    def clear(self):
        self.Enemies = {"cockroach":[]}

    def clear_type(self,Type):
        self.Enemies[Type].clear()

    def remove(self,x,y):
        output = []
        for Type in list(self.Enemies.keys()):
            for enem in self.Enemies[Type]:
                if enem.position.xy == (x,y):
                    self.Enemies[Type].pop(self.Enemies[Type].index(enem))
                    break

    def get_count(self):
        output = 0
        for Type in list(self.Enemies.keys()):
            output += len(self.Enemies[Type])
        return output

    def add_Enemie(self,Type,display,position,width,height):
        if Type == "cockroach":
            self.Enemies[Type].append(cockroach(self,display,position,width,height,self.Enemie1))


class cockroach(Surface):
    def __init__(self,display,position,width,height,sprites):
        super().__init__(display, position, (width),height = height)

        self.sprites = sprites
        self.original_surface.blit(self.sprites["cleft"],(0,0))
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
