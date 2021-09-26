import pygame
import sys
import os
from random import choice

import pickle

from screener import adjuster

from tile import *

from main_menu import *

from player import Player

class level_importer(Surface):
    def __init__(self, SCREEN):
        super().__init__(SCREEN, SCREEN.get_rect().center, SCREEN.get_width(),height = SCREEN.get_height())

        Adjuster = adjuster(self.DISPLAY_WIDTH,self.DISPLAY_HEIGHT)
        self.Adjuster = Adjuster

        self.update_surface()

        #textures
        self.Cavemen = {}
        for file in os.listdir(path="textures/cavemen"):
            self.Cavemen[file.replace(".png","")] = pygame.image.load(f'textures/cavemen/{file}')
            self.Cavemen[file.replace(".png","")] = pygame.transform.scale(self.Cavemen[file.replace(".png","")], Adjuster.get_surface_size((80,60)))

        #seting up the tile manager
        self.Tile_Manager = tile_manager({})
        names = ["ice","stone","sand","snow","grass","coble","stump"]
        for name in names:
            self.Tile_Manager.add_sprite(name,Adjuster)

        #setting up the main_menu.
        self.Menu_Manager = menu_manager()
        self.font = pygame.font.Font("freesansbold.ttf", Adjuster.get_surface_size((60,24))[0])

        self.player = Player(self.surface, self.get_rect().center,self.Cavemen)
        self.player.controlled = False

        self.player.position[0] = 10000

        self.Level = {'tile':[],'player':[],'text':[],'enemies':[]}

        self.buttons_pressed = []

        self.selected = "" 

    def save(self):
        with open(f"levels/player_save.txt","wb") as fp:
            pickle.dump(self.Level, fp)


        self.Level = {'tile':[],'player':[],'text':[],'enemies':[]}
        self.player.position.x = 100000
        self.Menu_Manager.remove_all_buttons()
        self.Menu_Manager.remove_all_labels()
        self.Tile_Manager.remove_all_tiles()

    def load(self):

        self.Level = {'tile':[],'player':[],'text':[],'enemies':[]}
        self.player.position.x = 100000
        self.Menu_Manager.remove_all_buttons()
        self.Menu_Manager.remove_all_labels()
        self.Tile_Manager.remove_all_tiles()

        with open("levels/level_list.txt","r") as num:
            level_name = choice(num.read().split("\n"))

        with open(f"levels/{level_name}.txt","rb") as fp:
            self.Level = pickle.load(fp)

        try:
            for tile in self.Level["tile"]:
                self.Tile_Manager.add_tile(self.surface,self.Adjuster.get_surface_size(tile[1]),tile[2],tile[3])

        except:
            print("error tile")

        try:
            for player in self.Level["player"]:
                self.player = self.player = Player(self.surface,self.Adjuster.get_surface_size(player[0]) ,self.Cavemen)

        except:
            print('error player')

        print("import ended")


    def update(self):

        self.surface.fill((0, 0, 1))

        #update classes
        self.player = self.Tile_Manager.update(self.player)
        self.Menu_Manager.update()
        self.player.update()
        self.player.draw()