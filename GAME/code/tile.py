import pygame
from pygame.locals import *
from surface import Surface

class tile_manager():
    def __init__(self,sprites):
        #the image is a dict of all the types of the tiles.
        self.sprites = sprites
        self.tiles = []

    def add_tile(self,x,y,img_name,wall):
        # the wall is boolen
        size = self.sprites[img_name].size
        sprite = self.sprites[img_name]
        self.tiles.append(Tile((x,y),sprite,wall))

    def remove_tile(self,x,y,w,h,wall):
        # the wall is boolen
        tile_to_remove = Rect(left, top, width, height)
        for tile in self.tiles.items():
            if tile[1].collide(tile_to_remove) and tile[1].get_wall() == wall:
                self.tiles.pop(tile[0])
                break

    def remove_all_walls():
        pass

    def update(self,player):
        for tile in self.tiles:
            player = tile.update(player)

    def add_sprite(self,sprite_name,adujuster):
        self.sprites[sprite_name] = pygame.image.load(f'textures/{sprite_name}.png')
        self.sprites[sprite_name] = pygame.transform.scale(self.sprites[sprite_name],adujuster.get_surface_size((90,90)))



class Tile(Surface):
    def __init__(self, position ,sprite ,wall):
        super().__init__(display, position, (sprite.width()))
        self.blit(sprite, (0 ,0))
        self.update_surface()

        self.wall = wall

    def get_wall():
        return self.wall
