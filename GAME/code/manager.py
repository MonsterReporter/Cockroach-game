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

        self.screenstates = {"game": self.game_loop,"main_menu": self.main_menu, "transition": self.transition_loop}
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

        self.font = pygame.font.Font("freesansbold.ttf", Adjuster.get_surface_size((60,24))[0])

        self.Menu_Manager.add_button(self.SCREEN ,Adjuster.get_surface_size((1920/2,400)) ,"play" ,self.font, "button")
        self.Menu_Manager.add_label(self.SCREEN ,Adjuster.get_surface_size((1920/2,300)) ,"Cock and roach : forever" ,self.font, "label")

        #import textures
        self.Cavemen = {}
        for file in os.listdir(path="textures/cavemen"):
            self.Cavemen[file.replace(".png","")] = pygame.image.load(f'textures/cavemen/{file}')
            self.Cavemen[file.replace(".png","")] = pygame.transform.scale(self.Cavemen[file.replace(".png","")], Adjuster.get_surface_size((80,60)))

        self.Cockroach = {}
        for file in os.listdir(path="textures/cockroach"):
            self.Cockroach[file.replace(".png","")] = pygame.image.load(f'textures/cockroach/{file}')

        self.cover = pygame.image.load(f'textures/cover.png')
        self.cover = pygame.transform.scale(self.cover,Adjuster.get_surface_size((1920,1080)))



        self.player = Player(self.SCREEN, self.SCREEN_CENTER,self.Cavemen)

        self.transition_endstate = None
        self.TRANSITION = pygame.USEREVENT + 0
        pygame.time.set_timer(self.TRANSITION, 2000)

    def game_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (pygame.key.get_pressed()[pygame.K_ESCAPE]):
                pygame.quit()
                sys.exit()
        
        self.SCREEN.fill((0, 0, 255))

        self.player = self.Tile_Manager.update(self.player)

        self.player.update()
        self.player.draw()

        pygame.display.update()

    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (pygame.key.get_pressed()[pygame.K_ESCAPE]):
                pygame.quit()
                sys.exit()
                

        # self.SCREEN.fill((0, 0, 0))
        self.SCREEN.blit(self.cover,(0,0))

        self.Menu_Manager.update()
        pressed = self.Menu_Manager.get_pressed()

        try:
            if pressed["button"]:
                self.transition_to("game")
        except:
            pass


        pygame.display.update()

    def transition_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (pygame.key.get_pressed()[pygame.K_ESCAPE]):
                pygame.quit()
                sys.exit()
            if event.type == self.TRANSITION:
                self.screenstate = self.transition_endstate

        self.SCREEN.fill((255, 0, 0))

        pygame.display.update()

    def transition_to(self, state):
        pygame.event.clear(self.TRANSITION)
        self.transition_endstate = self.screenstates[state]
        self.screenstate = self.screenstates["transition"]

    def run(self):
        self.screenstate()
