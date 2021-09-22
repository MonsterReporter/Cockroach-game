import pygame
import sys
import os


from screener import adujuster

from player import Player

class Manager:
    def __init__(self, screen, clock):
        self.SCREEN = screen
        self.SCREEN_WIDTH = self.SCREEN.get_width()
        self.SCREEN_HEIGHT = self.SCREEN.get_height()
        self.SCREEN_CENTER = (int(self.SCREEN_WIDTH / 2), int(self.SCREEN_HEIGHT / 2))

        self.CLOCK = clock

        Adujuster = adujuster(self.SCREEN.get_width,self.SCREEN.get_height)

        self.screenstates = {"game": self.game_loop}
        self.screenstate = self.screenstates["game"]

        #import textures
        self.Walls = pygame.image.load('textures/ice.png')
        self.Walls = pygame.image.load('textures/stone.png')
        self.Walls = pygame.image.load('textures/sand.png')
        self.Walls = pygame.image.load('textures/snow.png')

        self.Cavemen = {}
        for file in os.listdir(path="textures/cavemen"):
            self.Cavemen[file.replace(".png","")] = pygame.image.load(f'textures/cavemen/{file}')
            self.Cavemen[file.replace(".png","")] = pygame.transform.scale(self.Cavemen[file.replace(".png","")], Adujuster.get_surface_size((80,60)))

        self.Cockroach = {}
        for file in os.listdir(path="textures/cockroach"):
            self.Cockroach[file.replace(".png","")] = pygame.image.load(f'textures/cockroach/{file}')

            



        self.player = Player(self.SCREEN, self.SCREEN_CENTER,self.Cavemen)

        self.font = pygame.font.SysFont("Arial", 24)

    def game_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (pygame.key.get_pressed()[pygame.K_ESCAPE]):
                pygame.quit()
                sys.exit()
        
        self.SCREEN.fill((0, 0, 0))

        self.player.update()
        self.player.draw()

        pygame.display.update()

    def run(self):
        self.screenstate()
