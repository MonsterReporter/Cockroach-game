import pygame
import sys

<<<<<<< Updated upstream
=======
from screen_ import adujuster

>>>>>>> Stashed changes
from player import Player

class Manager:
    def __init__(self, screen, clock):
        self.SCREEN = screen
        self.SCREEN_WIDTH = self.SCREEN.get_width()
        self.SCREEN_HEIGHT = self.SCREEN.get_height()
        self.SCREEN_CENTER = (int(self.SCREEN_WIDTH / 2), int(self.SCREEN_HEIGHT / 2))

        self.CLOCK = clock

        self.screenstates = {"game": self.game_loop}
        self.screenstate = self.screenstates["game"]

        self.player = Player(self.SCREEN, self.SCREEN_CENTER)

    def game_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        self.SCREEN.fill((0, 0, 0))

        self.player.update()
        self.player.draw()

        pygame.display.update()

    def run(self):
        self.screenstate()
