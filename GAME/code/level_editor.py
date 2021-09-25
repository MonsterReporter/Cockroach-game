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
        names = ["ice","stone","sand","snow"]
        for name in names:
            self.Tile_Manager.add_sprite(name,Adjuster)

        #setting up the main_menu.
        self.Menu_Manager = menu_manager()
        self.font = pygame.font.Font("freesansbold.ttf", Adjuster.get_surface_size((60,24))[0])

        self.player = Player(self.DISPLAY, self.get_rect().center,self.Cavemen)
        self.player.controlled = False

        self.player.position[0] = 10000

        self.Level = []

        self.buttons_pressed = []

    def save(self):
        with open("levels/num.txt","r") as num:
            number = int(num.read())
            with open("levels/num.txt","w") as numw:
                numw.write(str(number + 1))

        with open(f"levels/level{number}.txt","wb") as fp:
            pickle.dump(self.Level, fp)



    def update(self):


        #update classes
        self.player = self.Tile_Manager.update(self.player)
        self.Menu_Manager.update()
        self.player.update()
        self.player.draw()

        #manage level creation
        keys = pygame.key.get_pressed()
        pos = pygame.mouse.get_pos()
        pos_r = self.Adjuster.get_surface_size_reverse((pos))
        # pygame.draw.rect(self.surface, (255,0,0), pygame.Rect(pos[0],pos[1],20,20))

        if keys[pygame.K_LCTRL] and keys[pygame.K_1]:
            if not "1" in self.buttons_pressed:
                self.button_pressed("1")
                self.buttons_pressed.append("1")
        else:
            if "1" in self.buttons_pressed:
                self.buttons_pressed.pop(self.buttons_pressed.index("1"))

        if keys[pygame.K_LCTRL] and keys[pygame.K_2]:
            if not "2" in self.buttons_pressed:
                self.button_pressed("2")
                self.buttons_pressed.append("2")
        else:
            if "2" in self.buttons_pressed:
                self.buttons_pressed.pop(self.buttons_pressed.index("2"))

        if keys[pygame.K_LCTRL] and keys[pygame.K_3]:
            if not "3" in self.buttons_pressed:
                self.button_pressed("3")
                self.buttons_pressed.append("3")
        else:
            if "3" in self.buttons_pressed:
                self.buttons_pressed.pop(self.buttons_pressed.index("3"))

        if keys[pygame.K_LCTRL] and keys[pygame.K_4]:
            if not "4" in self.buttons_pressed:
                self.button_pressed("4")
                self.buttons_pressed.append("4")
        else:
            if "4" in self.buttons_pressed:
                self.buttons_pressed.pop(self.buttons_pressed.index("4"))

    def button_pressed(self, key):
        pos = pygame.mouse.get_pos()
        pos_r = self.Adjuster.get_surface_size_reverse((pos))

        if "1" == key:
            self.Level.append(["DISPLAY" ,pos_r ,"ice" ,True])
            self.Tile_Manager.add_tile(self.surface ,pos ,"ice" ,True)
        if "2" == key:
            self.Level.append(["DISPLAY" ,pos_r ,"stone" ,True])
            self.Tile_Manager.add_tile(self.surface ,pos ,"stone" ,True)

        if "3" == key:
            self.Level.append(["DISPLAY" ,pos_r ,"sand" ,False])
            self.Tile_Manager.add_tile(self.surface ,pos ,"sand" ,False)

        if "4" == key:
            self.Level.append(["DISPLAY" ,pos_r ,"snow" ,False])
            self.Tile_Manager.add_tile(self.surface ,pos ,"snow" ,False)


