def main():
    import pygame

    import sys
    import os
    sys.path.append(os.path.join(os.getcwd(),"code")) 

    # from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FRAMERATE
    import screener
    from manager import Manager

    pygame.init()

    SCREEN = screener.set_up_screen()
    CLOCK = pygame.time.Clock()

    manager = Manager(SCREEN, 60)

    while(1):
        manager.run()
        CLOCK.tick(60)

if __name__ == "__main__":
    main()