import pygame
import sys
import os
import webbrowser as web



from screener import adjuster

from tile import *

from main_menu import *

from level_editor import *

from level_importer import *

from player import Player

class Manager:
    def __init__(self, screen, clock):
        self.SCREEN = screen
        self.SCREEN_WIDTH = self.SCREEN.get_width()
        self.SCREEN_HEIGHT = self.SCREEN.get_height()
        self.SCREEN_CENTER = (int(self.SCREEN_WIDTH / 2), int(self.SCREEN_HEIGHT / 2))

        self.CLOCK = clock

        Adjuster = adjuster(self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
        self.Adjuster = Adjuster

        self.screenstates = {"game": self.game_transition,"main_menu": self.main_menu, 
            "transition": self.transition_loop,
            "level_creator" : self.level_ediotor,
            "game_loop": self.game_loop,
            "credits" : self.credits
            }
        self.screenstate = self.screenstates["main_menu"]

        #seting up the tile manager
        self.Tile_Manager = tile_manager({})
        names = ["ice","stone","sand","snow","grass","coble","stump"]
        for name in names:
            self.Tile_Manager.add_sprite(name,Adjuster)

        #testing tiles.
        self.Tile_Manager.add_tile(self.SCREEN,Adjuster.get_surface_size((100,100)),"ice",True)

        #setting up the main_menu.
        self.Menu_Manager = menu_manager()

        self.font = pygame.font.Font("freesansbold.ttf", Adjuster.get_surface_size((60,24))[0])

        self.Menu_Manager.add_button(self.SCREEN ,Adjuster.get_surface_size((1920/2,400)) ,"play" ,self.font, "button")
        self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((100,1080 * 19 / 20)) ,"exit" ,self.font, "esc")
        self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,500)) ,"credits" ,self.font, "credits")
        self.Menu_Manager.add_label(self.SCREEN ,Adjuster.get_surface_size((1920/2,300)) ,"Coakroach : forever" ,self.font, "label")



        #import textures
        self.Cavemen = {}
        for file in os.listdir(path="textures/cavemen"):
            self.Cavemen[file.replace(".png","")] = pygame.image.load(f'textures/cavemen/{file}')
            self.Cavemen[file.replace(".png","")] = pygame.transform.scale(self.Cavemen[file.replace(".png","")], Adjuster.get_surface_size((80,60)))
        self.Bow = []
        self.Bow.append(pygame.image.load(f'textures/bows/bow3.png'))
        self.Bow.append(pygame.image.load(f'textures/bows/arrow.png'))
        self.Bow[0] = pygame.transform.scale(self.Bow[0], Adjuster.get_surface_size((39,21)))
        self.Bow[1] = pygame.transform.scale(self.Bow[1], Adjuster.get_surface_size((15,24)))

        self.Cockroach = {}
        for file in os.listdir(path="textures/cockroach"):
            self.Cockroach[file.replace(".png","")] = pygame.image.load(f'textures/cockroach/{file}')

        self.cover = pygame.image.load(f'textures/cover.png')
        self.cover = pygame.transform.scale(self.cover,Adjuster.get_surface_size((1920,1080)))

        #setting up the level_creator
        self.Level_Creator = level_creator(self.SCREEN)

        #setting up level_importer
        self.Level_Importer = level_importer(self.SCREEN)

        #load player

        self.player = Player(self.SCREEN, self.SCREEN_CENTER,self.Cavemen,self.Bow)

        #setup transtions
        self.transition_endstate = None
        self.TRANSITION = pygame.USEREVENT + 0
        pygame.time.set_timer(self.TRANSITION, 2000)

        #setup muisc
        pygame.mixer.init()
        self.main = pygame.mixer.Sound("music/main.mp3")
        self.main3 = pygame.mixer.Sound("music/main.wav")
        self.overworld = pygame.mixer.Sound("music/Overworld.wav")

        #Starting up
        self.transition_to("main_menu")

    def game_transition(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.Level_Importer.load()
        self.transition_to("game_loop")

    def game_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if  (pygame.key.get_pressed()[pygame.K_ESCAPE]):
                self.transition_to("main_menu")

        self.Level_Importer.update()
        self.Level_Importer.draw()

        pygame.display.update()

    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (pygame.key.get_pressed()[pygame.K_ESCAPE]):
                pygame.quit()
                sys.exit()

            if (pygame.key.get_pressed()[pygame.K_l]):
                self.transition_to("level_creator") 

            if (pygame.key.get_pressed()[pygame.K_c]):
                self.Menu_Manager.clear()
                self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,1080* 3 / 4)) ,"back" ,self.font, "button")
                self.Menu_Manager.add_label(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,300)) ,"Credits" ,self.font, "label")

                self.Menu_Manager.add_label(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,400)) ,"developers" ,self.font, "label")
                self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,450)) ,"catornot" ,self.font, "catornot")
                self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,510)) ,"Intense" ,self.font, "Intense")

                self.Menu_Manager.add_label(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,600)) ,"Artist" ,self.font, "label")
                self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,650)) ,"MonsterReporter" ,self.font, "MonsterReporter")
                self.transition_to("credits")              

        # self.SCREEN.fill((0, 0, 0))
        pygame.display.update()

        self.SCREEN.blit(self.cover,(0,0))

        self.Menu_Manager.update()
        pressed = self.Menu_Manager.get_pressed()

        try:
            if pressed["button"]:
                self.transition_to("game")
                
        except:
            pass


        try:
            if pressed["esc"]:
                font = pygame.font.Font("freesansbold.ttf", self.Adjuster.get_surface_size((200,24))[0])
                self.Menu_Manager.add_label(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,1080/2)) ,"Press ESC" ,font, "label")

        except:
            self.Menu_Manager.remove_all_labels()
            self.Menu_Manager.add_label(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,300)) ,"Coakroach : forever" ,self.font, "label")

        try:
            if pressed["credits"]:
                self.Menu_Manager.clear()
                self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,1080* 3 / 4)) ,"back" ,self.font, "button")
                self.Menu_Manager.add_label(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,300)) ,"Credits" ,self.font, "label")

                self.Menu_Manager.add_label(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,400)) ,"developers" ,self.font, "label")
                self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,450)) ,"catornot" ,self.font, "catornot")
                self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,510)) ,"Intense" ,self.font, "Intense")

                self.Menu_Manager.add_label(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,600)) ,"Artist" ,self.font, "label")
                self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,650)) ,"MonsterReporter" ,self.font, "MonsterReporter")
                self.transition_to("credits")
        except:
            pass

    def credits(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if  (pygame.key.get_pressed()[pygame.K_ESCAPE]):
                self.Menu_Manager.clear()
                self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((100,1080 * 19 / 20)) ,"exit" ,self.font, "esc")
                self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,400)) ,"play" ,self.font, "button")
                self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,500)) ,"credits" ,self.font, "credits")
                self.Menu_Manager.add_label(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,300)) ,"Coakroach : forever" ,self.font, "label")
                self.transition_to("main_menu")


        self.SCREEN.fill((255,190,168))

        self.Menu_Manager.update()
        pressed = self.Menu_Manager.get_pressed()

        try:
            if pressed["button"]:
                self.Menu_Manager.clear()
                self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,400)) ,"play" ,self.font, "button")
                self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((100,1080 * 19 / 20)) ,"exit" ,self.font, "esc")
                self.Menu_Manager.add_button(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,500)) ,"credits" ,self.font, "credits")
                self.Menu_Manager.add_label(self.SCREEN ,self.Adjuster.get_surface_size((1920/2,300)) ,"Coakroach : forever" ,self.font, "label")
                self.transition_to("main_menu")
        except:
            pass

        try:
            if pressed["catornot"]:
                web.open("https://github.com/catornot")
        except:
            pass

        try:
            if pressed["Intense"]:
                web.open("https://github.com/ItsIntense/")
        except:
            pass

        try:
            if pressed["MonsterReporter"]:
                web.open("https://github.com/MonsterReporter")
        except:
            pass


        pygame.display.update()

    def level_ediotor(self):
        for event in pygame.event.get():
            if (pygame.key.get_pressed()[pygame.K_BACKSPACE]):
                pygame.quit()
                sys.exit()

            if event.type == pygame.QUIT:
                self.Level_Creator.save()
                pygame.quit()
                sys.exit()
            if (pygame.key.get_pressed()[pygame.K_ESCAPE]) or (pygame.key.get_pressed()[pygame.K_LCTRL] and pygame.key.get_pressed()[pygame.K_s]):
                self.Level_Creator.save()
                self.transition_to("main_menu")

        self.SCREEN.fill((0, 0, 0))
        
        self.Level_Creator.update()
        self.Level_Creator.draw()

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
        pygame.mixer.fadeout(20)
        if state == "main_menu":
            self.main3.play(loops=100000)
        if state == "credits":
            self.main.play(loops=100000)
        if state == "game_loop":
            self.overworld.play(loops=100000)

    def run(self):
        self.screenstate()
