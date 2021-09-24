import pygame

class Surface:
    def __init__(self, display, position, size, colorkey=(0, 0, 0),height = None):
        self.DISPLAY = display
        self.DISPLAY_WIDTH = display.get_width()
        self.DISPLAY_HEIGHT = display.get_height()

        if height == None:
            self.original_surface = pygame.Surface((size, size))
        else:
            self.original_surface = pygame.Surface((size, height))
        self.original_surface.set_colorkey(colorkey)
        self.position = pygame.Vector2(position)

        self.update_surface()

    def update_surface(self):
        self.surface = self.original_surface.copy()
    
    def draw(self):
        self.DISPLAY.blit(self.surface, self.surface.get_rect(center=self.position))
    
    def get_size(self):
        return self.surface.get_width()
    
    def get_half(self):
        return self.get_surface.get_width() / 2
    
    def get_rect(self):
        return self.surface.get_rect(center=self.position)
    
    def collide(self, surface):
        rect_1 = self.surface.get_rect()
        rect_2 = surface.get_rect()
        return rect_1.colliderect(rect_2)
