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

    def remove_tile(self,pos):
        # the wall is boolen
        for tile in self.tiles:
            if tile.get_rect().collidepoint(pos):
                self.tiles.pop(self.tiles.index(tile))
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
        pygame.draw.rect(self.original_surface, (100,100,100), (0,0,display.get_width(),display.get_width()) ,1 , border_radius=1)
        self.update_surface()

        self.wall = wall

    def get_wall(self):
        return self.wall

    def update(self ,player):
        if self.get_wall():

            player_rect = player.get_rect()

            if player.get_rect().colliderect(self.surface.get_rect()):

                # self.rect = pygame.Rect(self.get_rect().left + offset, self.get_rect().top, player.get_width(), player.get_width())

                if player.position[0] > self.position[0]:
                    player_rect.right = self.get_rect().left
                    player.stop_velocity_x()

                elif player.position[0] < self.position[0]:
                    player_rect.left = self.get_rect().right
                    player.stop_velocity_x()

                if player.position[1] > self.position[1]:
                    player_rect.bottom = self.get_rect().top
                    player_rect.centerx = player_rect.top - self.get_rect().bottom
                    player.stop_velocity_y()

                elif player.position[1] < self.position[1]:
                    player_rect.centerx = player_rect.bottom - self.get_rect().top
                    player.stop_velocity_y()


                # if player.position[0] > self.position[0]:
                #     player_rect.right = self.get_rect().left
                #     player.stop_velocity_x()

                # elif player.position[0] < self.position[0]:
                #     player_rect.left = self.get_rect().right
                #     player.stop_velocity_x()

                # if player.position[1] > self.position[1]:
                #     player_rect.bottom = self.get_rect().top
                #     player.stop_velocity_y()

                # elif player.position[1] < self.position[1]:
                #     player_rect.top = self.get_rect().bottom
                #     player.stop_velocity_y()

                player.position[0] = player_rect.centerx
                player.position[1] = player_rect.centery

        return player
