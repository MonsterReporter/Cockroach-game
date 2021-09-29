import pygame
import sys
import os
from random import choice

import pickle

from code_base.setup import adjuster

from code_base.tile import *

from main_menu import *

from player import Player

from enemies import enemy_manager

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

        self.Bow = []
        self.Bow.append(pygame.image.load(f'textures/bows/bow3.png'))
        self.Bow.append(pygame.image.load(f'textures/bows/arrow.png'))
        self.Bow[0] = pygame.transform.scale(self.Bow[0], Adjuster.get_surface_size((39,21)))
        self.Bow[1] = pygame.transform.scale(self.Bow[1], Adjuster.get_surface_size((15,24)))

        #sound effects
        self.sound = []
        self.sound.append(pygame.mixer.Sound("music/walk.wav"))
        self.sound.append(pygame.mixer.Sound("music/walk2.wav"))
        self.sound.append(pygame.mixer.Sound("music/arrow_hit.wav"))
        self.sound.append(pygame.mixer.Sound("music/arrow_shoot.wav"))

        #seting up the tile manager
        self.Tile_Manager = tile_manager({})
        names = ["ice","stone","sand","snow","grass","coble","stump"]
        for name in names:
            self.Tile_Manager.add_sprite(name,Adjuster)

        #seting up enemy manager
        self.Cockroach = {}
        for file in os.listdir(path="textures/cockroach"):
            self.Cockroach[file.replace(".png","")] = pygame.image.load(f'textures/cockroach/{file}')
            self.Cockroach[file.replace(".png","")] = pygame.transform.scale(self.Cockroach[file.replace(".png","")], Adjuster.get_surface_size((57,66)))

        self.Enemy_Manager = enemy_manager(self.surface,self.Cockroach)

        #setting up the main_menu.
        self.Menu_Manager = menu_manager()
        self.font = pygame.font.Font("freesansbold.ttf", Adjuster.get_surface_size((60,24))[0])

        self.player = Player(self.surface, self.get_rect().center,self.Cavemen,self.Bow,self.sound)
        self.player.controlled = False

        self.player.position[0] = 10000

        self.Level = {'tile':[],'player':[],'text':[],'enemies':[]}

        self.buttons_pressed = []

        self.selected = "" 

        self.start_ticks=pygame.time.get_ticks()
        self.sec = 0
        self.wait = False

    def save(self):
        with open(f"levels/player_save.txt","wb") as fp:
            pickle.dump(self.Level, fp)


        self.Level = {'tile':[],'player':[],'text':[],'enemies':[]}
        self.player.position.x = 100000
        self.Menu_Manager.remove_all_buttons()
        self.Menu_Manager.remove_all_labels()
        self.Tile_Manager.remove_all_tiles()
        self.Enemy_Manager.clear()

    def load(self):

        self.Level = {'tile':[],'player':[],'text':[],'enemies':[]}
        self.player.position.x = 100000
        self.Menu_Manager.remove_all_buttons()
        self.Menu_Manager.remove_all_labels()
        self.Tile_Manager.remove_all_tiles()
        self.Enemy_Manager.clear()

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
            for enem in self.Level["enemies"]:
                self.Enemy_Manager.add_Enemie(self.surface,enem[1],self.Adjuster.get_surface_size(enem[2]),enem[3])

        except:
            print('error enemie')

        try:
            for player in self.Level["player"]:
                self.player = self.player = Player(self.surface,self.Adjuster.get_surface_size(player[0]) ,self.Cavemen,self.Bow,self.sound)

        except:
            print('error player')

        print("import ended")


    def update(self):

        self.surface.fill((0, 0, 1))

        #update classes
        self.Tile_Manager.update(self.player)
        self.Menu_Manager.update()
        cords2 = self.Enemy_Manager.update(self.Tile_Manager.get_walls(),self.player)
        cords = self.player.update(walls = self.Tile_Manager.get_walls(), enemies = self.Enemy_Manager.get_enemies_all())
        self.player.draw()

        if cords != None:
            self.Enemy_Manager.remove(cords)
        if cords2 != None:
            if self.player.get_rect().collidepoint(cords2):
                return True


        if self.Enemy_Manager.get_count() == 0:
            self.start_ticks=pygame.time.get_ticks()
            self.sec = 5
            self.wait = True
            return True

        # if self.sec < (pygame.time.get_ticks()-self.start_ticks)/1000 and self.wait:
        #     return True

        return False
