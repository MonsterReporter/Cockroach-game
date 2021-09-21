<<<<<<< Updated upstream
import sys
import os
sys.path.append(os.path.join(os.getcwd(),"code")) 

# icon
# icon = pygame.image.load("none")
# pygame.display.set_icon(icon)

# # title
# pygame.display.set_caption("game")


=======
>>>>>>> Stashed changes
def main():
    import sys
    import os
    sys.path.append(os.path.join(os.getcwd(),"code")) 
    
    import pygame

    # from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FRAMERATE
    from screen_ import *
    from manager import Manager

    pygame.init()

    SCREEN = set_up_scree()
    CLOCK = pygame.time.Clock()

    manager = Manager(SCREEN, CLOCK)

    while(1):
        manager.run()
        CLOCK.tick(60)

if __name__ == "__main__":
    main()