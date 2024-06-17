import pygame as pg
import sys
from constants import *
from map import *
from hero import *
from raycasting import *
from objects import *
from sprite import *
from game_manager import *
from weapon import *

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(res)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger =False
        self.global_event = pg.USEREVENT
        pg.time.set_timer(self.global_event, 50)
        self.game()

    def game(self):
        self.map = Map(self)
        self.hero = Hero(self)
        self.objects = Objects(self)
        self.raycasting = RayCasting(self)
        self.manager = GameManager(self)
        self.weapon = Weapon(self)
        self.pathfinding = PathFinding(self)


    def update(self):
        self.hero.update()
        self.raycasting.update()
        self.manager.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(fps)

    def create(self):
        self.objects.draw()
        self.weapon.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.hero.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.create()

if __name__ == '__main__':
    game = Game()
    game.run()