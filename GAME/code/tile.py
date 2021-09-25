import pygame
import math
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
        self.update_surface()

        self.wall = wall

    def get_wall(self):
        return self.wall

    def distance(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))

    def circle_collision(self,rect,self_rect):
        self_rect.width = self_rect.width / 4

        distance = self.distance(rect.centerx, rect.centery, self_rect.centerx, self_rect.centery)

        if distance <= self_rect.width + rect.width:
            if rect.centerx > self_rect.centerx:
                rect.setx += self_rect.width + rect.width - distance

            elif rect.centerx < self_rect.centerx:
                rect.centerx -= self_rect.width + rect.width - distance

            if rect.centery > self_rect.centery:
                rect.centery += self_rect.width + rect.width - distance

            elif rect.centery < self_rect.centery:
                rect.centery -= self_rect.width + rect.width - distance

        return rect

    def update(self ,player):
        if self.get_wall():

            # player_rect = player.get_rect()

            # rect = player.box

            # self_rect = self.get_rect()

            # if player_rect.colliderect(self.get_rect()):
            #     if player.velocity.x < 0:
            #         player.position.x = self.get_rect().right + self.get_half()[0]
            #     elif player.velocity.x > 0:
            #         player.position.x = self.get_rect().left - self.get_half()[0]
            #     player.velocity.update(0, 0)

            # player_rect = player.get_rect()
                
            # if player_rect.colliderect(self.get_rect()):
            #     if player.velocity.y < 0:
            #         player.position.y = self.get_rect().bottom + self.get_half()[1]
            #     elif player.velocity.y > 0:
            #         player.position.y = self.get_rect().top - self.get_half()[1]
            #     player.velocity.update(0, 0)

            # if rect.colliderect(self_rect):

                # print(rect.center,"\n========")

                # if rect.x > self_rect.x: # Moving right; Hit the left side of the wall
                #     # rect.right = self_rect.left
                #     rect.centerx += rect.centerx - self_rect.centerx
                # if rect.x < self_rect.x: # Moving left; Hit the right side of the wall
                #     # rect.left = self_rect.right
                #     rect.centerx -= rect.centerx + self_rect.centerx
                # if rect.y > self_rect.x: # Moving down; Hit the top side of the wall
                #     # rect.bottom = self_rect.top
                #     rect.centery += rect.centery - self_rect.centery
                # if rect.y < self_rect.x: # Moving up; Hit the bottom side of the wall
                #     # rect.top = self_rect.bottom
                #     rect.centery -= rect.centery  + self_rect.centery



                # new_self_rect = rect
                # new_self_rect.centery += self_rect.width / 4
                # new_self_rect.centerx += self_rect.width / 4
                # rect = self.circle_collision(rect,new_self_rect)

                # new_self_rect = rect
                # new_self_rect.centery += self_rect.width / 4
                # new_self_rect.centerx -= self_rect.width / 4
                # rect = self.circle_collision(rect,new_self_rect)

                # new_self_rect = rect
                # new_self_rect.centery -= self_rect.width / 4
                # new_self_rect.centerx -= self_rect.width / 4
                # rect = self.circle_collision(rect,new_self_rect)

                # new_self_rect = rect
                # new_self_rect.centery -= self_rect.width / 4
                # new_self_rect.centerx += self_rect.width / 4
                # rect = self.circle_collision(rect,new_self_rect)

                # print(rect.center)

                # player.position.xy = rect.center
            
            x = player.position.x + math.cos(player.direction)
            y = player.position.y + math.sin(player.direction)
            if self.get_rect().collidepoint(x,y):
                player.block_key(pygame.K_w)

                keys = pygame.key.get_pressed()
                if not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
                    player.stop_velocity_x()
                    player.stop_velocity_y()




                
                
        return player
