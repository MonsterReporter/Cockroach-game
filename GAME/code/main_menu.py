import pygame
from pygame.locals import *
from surface import Surface

class menu_manager():
    def __init__(self):
        #the image is a dict of all the types of the buttons.
        self.buttons = []
        self.labels = []

    def add_button(self ,display ,position ,text ,font, name ,Adjuster):
        self.buttons.append(button(display ,position ,text ,font, name ,Adjuster))

    def add_label(self ,display ,position ,text ,font, name ,Adjuster):
        self.labels.append(label(display ,position ,text ,font, name ,Adjuster))

    def remove_all_buttons(self):
        self.buttons.clear()

    def remove_all_labels(self):
        self.labels.clear()

    def update(self):
        if self.get_button_amount() != 0:
            for button in self.buttons:
                button.update()
                button.draw()
        if self.get_label_amount() != 0:
            for label in self.labels:
                    label.draw()

    def get_label_amount(self):
        return len(self.labels)

    def get_button_amount(self):
        return len(self.buttons)

    def get_pressed(self):
        output = {}
        for button in self.buttons:
            if button.get_pressed:
                output[button.name] = button

        return output



class button(Surface):
    def __init__(self,display ,position ,text ,font, name ,Adjuster):
        text = font.render(text, True, (0, 0, 0))
        text = pygame.transform.scale(text ,Adjuster.get_surface_size(text.get_size()))
        text_rect = text.get_rect()
        text_rect.x = 0
        text_rect.y = 0

        super().__init__(display, position, text.get_width(),height = text.get_height())

        self.original_surface.blit(text, text_rect)
        pygame.draw.rect(self.original_surface, (0,0,0), text_rect)
        self.update_surface()

        self.name = name

        self.pressed = False

        self.text_rect = text_rect

    def update(self):
        print(self.position)
        if pygame.mouse.get_pressed()[0] and self.get_rect().collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.surface, (150,150,150), self.text_rect)

            self.pressed = True
        else:
            pygame.draw.rect(self.surface, (0,0,0), self.text_rect)

            self.pressed = False


class label(Surface):
    def __init__(self,display ,position ,text ,font, name ,Adjuster):
        text = font.render(text, True, (0, 0, 0))
        text = pygame.transform.scale(text ,Adjuster.get_surface_size(text.get_size()))
        text_rect = text.get_rect()
        text_rect.x = 0
        text_rect.y = 0

        super().__init__(display, position, text.get_width(),height = text.get_height())

        self.original_surface.blit(text, text_rect)
        self.update_surface()

        self.name = name
