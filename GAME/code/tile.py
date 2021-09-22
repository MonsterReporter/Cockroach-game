import pygame
from pygame.locals import *
from surface import Surface

class tile_manager():
    def __init__(self,sprites):
        #the image is a dict of all the types of the tiles.
        self.sprites = sprites
        self.tiles = []

    def add_tile(self ,display ,position ,img_name ,wall ):
        # the wall is boolen
        sprite = self.sprites[img_name]
        self.tiles.append(Tile(display ,position ,sprite ,wall ))

    def remove_tile(self,x,y,w,h,wall):
        # the wall is boolen
        tile_to_remove = Rect(x, y, w, h)
        for tile in self.tiles:
            if tile.collide(tile_to_remove) and tile.get_wall() == wall:
                self.tiles.pop(self.index(tile))
                break

    def remove_all_walls(self):
        for tile in self.tiles:
            if tile.get_wall():
                self.tiles.pop(self.index(tile))

    def remove_all_floor(self):
        for tile in self.tiles:
            if not tile.get_wall():
                self.tiles.pop(self.index(tile))

    def remove_all_tiles(self):
        self.tiles.clear()

    def update(self ,player):
        if self.get_tile_amount() != 0:
            for tile in self.tiles:
                player = tile.update(player)
                tile.draw()

        return player

    def get_tile_amount(self):
        return len(self.tiles)

    def add_sprite(self,sprite_name,adjuster):
        self.sprites[sprite_name] = pygame.image.load(f'textures/{sprite_name}.png')
        self.sprites[sprite_name] = pygame.transform.scale(self.sprites[sprite_name],adjuster.get_surface_size((90,90)))



class Tile(Surface):
    def __init__(self,display ,position ,sprite ,wall):
        super().__init__(display, position, (sprite.get_width()))

        self.original_surface.blit(sprite, (0 ,0))
        self.update_surface()

        self.wall = wall

    def get_wall(self):
        return self.wall

    def update(self ,player):
        if self.get_wall():

            if player.collide(self.surface):
                if player.position[0] > self.position[0]:
                    player.position[0] += 2
                    # player.position[0] += (self.position[0] + self.get_size) - + 2
                    # P.append_to_keys_blocked("a")

                elif player.position[0] < self.position[0]:
                    player.position[0] -= 2
                    # player.position[0] -= (self.position[0] + self.get_size) + P.radius - + 2
                    # P.append_to_keys_blocked("d")

                if player.position[1] > self.position[1]:
                    player.position[1] += 2
                    # player.position[1] += (self.position[1] + self.get_size) + player.position[1]. - + 2
                    # P.append_to_keys_blocked("w")

                elif player.position[1] < self.position[1]:
                    player.position[1] -= 2
                    # player.position[1] -= self.radius + P.radius - + 2
                    # P.append_to_keys_blocked("s")

        return player
