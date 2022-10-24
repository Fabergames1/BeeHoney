from obj import Obj
import pygame


class Menu:

    def __init__(self, image):

        self.bg = Obj(image, 0, 0)

        self.change_scene = False

    def draw(self, window):
        self.bg.draw(window)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.change_scene = True


class GameOver(Menu):

    def __init__(self, image):
        super().__init__(image)



