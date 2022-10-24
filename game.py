from obj import Obj, Bee, Text
import random


class Game:

    def __init__(self):

        self.bg = Obj("assets/bg.png", 0, 0)
        self.bg2 = Obj("assets/bg.png", 0, -640)

        self.spider = Obj("assets/spider1.png", random.randrange(0, 320), -50)
        self.flower = Obj("assets/florwer1.png", random.randrange(0, 320), 200)
        self.bee = Bee("assets/bee1.png", 150, 600)

        self.change_scene = False

        self.score = Text(120, "0")
        self.lifes = Text(60, "3")

    def draw(self, window):

        self.bg.draw(window)
        self.bg2.draw(window)
        self.bee.draw(window)
        self.spider.draw(window)
        self.flower.draw(window)
        self.score.draw(window, 160, 50)
        self.lifes.draw(window, 50, 50)

    def update(self):

        self.move_bg()
        self.spider.anim("spider", 8, 5)
        self.flower.anim("florwer", 8, 3)
        self.bee.anim("bee", 2, 5)
        self.move_spiders()
        self.move_flower()
        self.bee.colision(self.spider.group, "Spider")
        self.bee.colision(self.flower.group, "Flower")
        self.gameover()
        self.score.update_text(str(self.bee.pts))
        self.lifes.update_text(str(self.bee.life))

    def move_bg(self):
        self.bg.sprite.rect[1] += 10
        self.bg2.sprite.rect[1] += 10

        if self.bg.sprite.rect[1] > 640:
            self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] > 0:
            self.bg2.sprite.rect[1] = -640

    def move_spiders(self):
        self.spider.sprite.rect[1] += 11

        if self.spider.sprite.rect[1] > 640:
            self.spider.sprite.kill()
            self.spider = Obj("assets/spider1.png", random.randrange(0, 320), -50)

    def move_flower(self):
        self.flower.sprite.rect[1] += 8

        if self.flower.sprite.rect[1] > 640:
            self.flower.sprite.kill()
            self.flower = Obj("assets/florwer1.png", random.randrange(0, 320), -100)

    def gameover(self):
        if self.bee.life <= 0:
            self.change_scene = True
