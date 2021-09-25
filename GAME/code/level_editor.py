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
        with open("levels/num.txt","r") as num:
            number = int(num.read())
            with open("levels/num.txt","w") as numw:
                numw.write(str(number + 1))

        with open(f"levels/level{number}.txt","wb") as fp:
            pickle.dump(self.Level, fp)


        self.Level = {'tile':[],'player':[],'text':[],'enemies':[]}
        self.player.position.x = 100000
        self.Menu_Manager.remove_all_buttons()
        self.Menu_Manager.remove_all_labels()
        self.Tile_Manager.remove_all_tiles()

    def laod()
        with open("levels/num.txt","r") as num:
            number = int(num.read())
            with open("levels/num.txt","w") as numw:
                numw.write(str(number + 1))

        with open(f"levels/level{number}.txt","wb") as fp:
            pickle.dump(self.Level, fp)


        self.Level = {'tile':[],'player':[],'text':[],'enemies':[]}
        self.player.position.x = 100000
        self.Menu_Manager.remove_all_buttons()
        self.Menu_Manager.remove_all_labels()
        self.Tile_Manager.remove_all_tiles()

    def update(self):

        self.surface.fill((0, 0, 1))

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

        if keys[pygame.K_LCTRL] and keys[pygame.K_5]:
            if not "5" in self.buttons_pressed:
                self.button_pressed("5")
                self.buttons_pressed.append("5")
        else:
            if "5" in self.buttons_pressed:
                self.buttons_pressed.pop(self.buttons_pressed.index("5"))

        if keys[pygame.K_LCTRL] and keys[pygame.K_6]:
            if not "6" in self.buttons_pressed:
                self.button_pressed("6")
                self.buttons_pressed.append("6")
        else:
            if "6" in self.buttons_pressed:
                self.buttons_pressed.pop(self.buttons_pressed.index("6"))

        if keys[pygame.K_LCTRL] and keys[pygame.K_7]:
            if not "7" in self.buttons_pressed:
                self.button_pressed("7")
                self.buttons_pressed.append("7")
        else:
            if "7" in self.buttons_pressed:
                self.buttons_pressed.pop(self.buttons_pressed.index("7"))



        if keys[pygame.K_LCTRL] and keys[pygame.K_p]:
            if not "p" in self.buttons_pressed:
                self.button_pressed("p")
                self.buttons_pressed.append("p")
        else:
            if "p" in self.buttons_pressed:
                self.buttons_pressed.pop(self.buttons_pressed.index("p"))


        if pygame.mouse.get_pressed()[0]:
            if not "mouse" in self.buttons_pressed:
                self.mouse_pressed(self.selected)
                self.buttons_pressed.append("mouse")
        else:
            if "mouse" in self.buttons_pressed:
                self.buttons_pressed.pop(self.buttons_pressed.index("mouse"))
            

        if pygame.mouse.get_pressed()[2]:
            self.delete(pos,pos_r)

    def delete(self,pos,pos_r):
        rect_r = pygame.Rect(pos_r,self.Adjuster.get_surface_size((90,90)))

        for tile in self.Level["tile"]:
            if rect_r.collidepoint(tile[1]):
                self.Tile_Manager.remove_tile(pos)
                self.Level['tile'].pop(self.Level['tile'].index(tile))
                print("tile gone")
                break

        for player in self.Level["player"]:
            if rect_r.collidepoint(player[0]):
                self.Level["player"].clear()
                self.player.position.x = 10000
                break


    def mouse_pressed(self, key):
        pos = pygame.mouse.get_pos()
        pos_r = self.Adjuster.get_surface_size_reverse((pos))

        if "1" == key:
            self.Level['tile'].append(["DISPLAY" ,pos_r ,"ice" ,True])
            self.Tile_Manager.add_tile(self.surface ,pos ,"ice" ,True)
        if "2" == key:
            self.Level['tile'].append(["DISPLAY" ,pos_r ,"stone" ,True])
            self.Tile_Manager.add_tile(self.surface ,pos ,"stone" ,True)

        if "3" == key:
            self.Level['tile'].append(["DISPLAY" ,pos_r ,"sand" ,False])
            self.Tile_Manager.add_tile(self.surface ,pos ,"sand" ,False)

        if "4" == key:
            self.Level['tile'].append(["DISPLAY" ,pos_r ,"snow" ,False])
            self.Tile_Manager.add_tile(self.surface ,pos ,"snow" ,False)

        if "5" == key:
            self.Level['tile'].append(["DISPLAY" ,pos_r ,"grass" ,False])
            self.Tile_Manager.add_tile(self.surface ,pos ,"grass" ,False)

        if "6" == key:
            self.Level['tile'].append(["DISPLAY" ,pos_r ,"coble" ,False])
            self.Tile_Manager.add_tile(self.surface ,pos ,"coble" ,False)

        if "7" == key:
            self.Level['tile'].append(["DISPLAY" ,pos_r ,"stump" ,True])
            self.Tile_Manager.add_tile(self.surface ,pos ,"stump" ,True)


        if "p" == key:
            self.Level["player"].append([pos_r])
            self.player.position[0],self.player.position[1] = pos[0],pos[1]

    def button_pressed(self, key):
        self.selected = key


