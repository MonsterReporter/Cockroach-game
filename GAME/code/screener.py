import pygame

class adjuster():
    def __init__(self,size_x,size_y):
        self._size_x = size_x
        self._size_y = size_y

    def get_size(self):
        return (self._size_x,self._size_y)
    def get_size_x(self):
        return self._size_x
    def get_size_y(self):
        return self._size_y
    def get_surface_size(self,size):
        #size is width, height
        # return (int(30 / size[0] * 1920),int( 60 / size[1] * 1080))
        return (int(size[0] / 1920 * self._size_x),int( size[1] / 1080 * self._size_y))

def set_up_screen():
    # Set up the window.
    with open("settings.txt","r") as file:
        file = list(file.read().split("\n"))

        size_x, size_y , full = 640, 480, False
        
        for i in file:
            if i.startswith("#"):
                file.pop(file.index(i))
            if i.startswith("FullScreen"):
                full = bool(int(i.split(":")[1]))
            if i.startswith("screenSize_x"):
                size_x = int(i.split(":")[1])
            if i.startswith("screenSize_y"):
                size_y = int(i.split(":")[1])

        size = (size_x,size_y)

        if full:
            screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
        else:
            screen = pygame.display.set_mode(size)

    return screen