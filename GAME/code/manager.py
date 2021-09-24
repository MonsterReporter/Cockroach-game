import pygame
import sys
import os


from screener import adjuster

from tile import *

from main_menu import *

from player import Player

class Manager:
    def __init__(self, screen, clock):
        self.SCREEN = screen
        self.SCREEN_WIDTH = self.SCREEN.get_width()
        self.SCREEN_HEIGHT = self.SCREEN.get_height()
        self.SCREEN_CENTER = (int(self.SCREEN_WIDTH / 2), int(self.SCREEN_HEIGHT / 2))

        self.CLOCK = clock

        Adjuster = adjuster(self.SCREEN_WIDTH,self.SCREEN_HEIGHT)

        self.screenstates = {"game": self.game_loop,"main_menu": self.main_menu}
        self.screenstate = self.screenstates["main_menu"]

        #seting up the tile manager
        self.Tile_Manager = tile_manager({})
        names = ["ice","stone","sand","snow"]
        for name in names:
            self.Tile_Manager.add_sprite(name,Adjuster)

        #testing tiles.
        self.Tile_Manager.add_tile(self.SCREEN,Adjuster.get_surface_size((100,100)),"ice",True)

        #setting up the main_menu.
        self.Menu_Manager = menu_manager()

        self.font = pygame.font.SysFont("Arial", Adjuster.get_surface_size((40,24))[0])

        self.Menu_Manager.add_button(self.SCREEN ,Adjuster.get_surface_size((300,300)) ,"test1" ,self.font, "button")
        self.Menu_Manager.add_label(self.SCREEN ,Adjuster.get_surface_size((300,320)) ,"test2" ,self.font, "label")

        #import textures
        self.Cavemen = {}
        for file in os.listdir(path="textures/cavemen"):
            self.Cavemen[file.replace(".png","")] = pygame.image.load(f'textures/cavemen/{file}')
            self.Cavemen[file.replace(".png","")] = pygame.transform.scale(self.Cavemen[file.replace(".png","")], Adjuster.get_surface_size((80,60)))

        self.Cockroach = {}
        for file in os.listdir(path="textures/cockroach"):
            self.Cockroach[file.replace(".png","")] = pygame.image.load(f'textures/cockroach/{file}')

            



        self.player = Player(self.SCREEN, self.SCREEN_CENTER,self.Cavemen)

    def game_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (pygame.key.get_pressed()[pygame.K_ESCAPE]):
                pygame.quit()
                sys.exit()
        
        self.SCREEN.fill((0, 0, 0))

        self.player = self.Tile_Manager.update(self.player)

        self.player.update()
        self.player.draw()

        pygame.display.update()

    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (pygame.key.get_pressed()[pygame.K_ESCAPE]):
                pygame.quit()
                sys.exit()

        self.SCREEN.fill((0, 0, 0))

        self.Menu_Manager.update()

        pygame.display.update()

    def run(self):
        self.screenstate()
