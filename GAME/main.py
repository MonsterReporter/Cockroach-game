def main():
    import pygame

    from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FRAMERATE
    from manager import Manager

    pygame.init()

    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    CLOCK = pygame.time.Clock()

    manager = Manager(SCREEN, CLOCK)

    while(1):
        manager.run()
        CLOCK.tick(FRAMERATE)

if __name__ == "__main__":
    main()
