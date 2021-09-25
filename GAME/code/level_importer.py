import pygame
import sys
import os

import pickle

from screener import adjuster

from tile import *

from main_menu import *

from player import Player

class level_creator(Surface):
    def __init__(self, SCREEN):
        super().__init__(SCREEN, SCREEN.get_rect().center, SCREEN.get_width(),height = SCREEN.get_height())

        Adjuster = adjuster(self.DISPLAY_WIDTH,self.DISPLAY_HEIGHT)
        self.Adjuster = Adjuster

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

        self.player = Player(self.DISPLAY, self.get_rect().center,self.Cavemen)
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