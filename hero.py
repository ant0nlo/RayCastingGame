import pygame as pg
import math
from constants import *

class Hero:
    def __init__(self, game):
        self.game = game
        self.x, self.y = hero_positions
        self.angle = hero_angle
        self.shot = False
        self.rel = 0
        self.health = hero_max_helth
        self.time_prev = pg.time.get_ticks()
        self.diag_move_corr = 1 / math.sqrt(2)

    def single_fire_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
        #if event.type == pg.KEYDOWN:
            # if event.key == pg.K_e and not self.shot and not self.game.weapon.reloading:
                self.shot = True
                self.game.weapon.reloading = True

    def check_game_over(self):
        if self.health < 1:
            self.game.objects.game_over()
            pg.display.flip()
            pg.time.delay(3000)

    def get_damage(self, damage):
        self.health -= damage
        self.game.objects.hero_damage()
        self.check_game_over()

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        speed = hero_speed * self.game.delta_time

        keys = pg.key.get_pressed()
        movements = {
            pg.K_w: (speed * cos_a, speed * sin_a),
            pg.K_s: (-speed * cos_a, -speed * sin_a),
            pg.K_a: (speed * sin_a, -speed * cos_a),
            pg.K_d: (-speed * sin_a, speed * cos_a),
        }

        dx, dy = 0, 0
        for key, (step_x, step_y) in movements.items():
            if keys[key]:
                dx += step_x
                dy += step_y

        self.check_wall_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= hero_speed * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += hero_speed * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
            scale = hero_size / self.game.delta_time
            if self.check_wall(int(self.x + dx * scale), int(self.y)):
                self.x += dx
            if self.check_wall(int(self.x), int(self.y + dy * scale)):
                self.y += dy

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < mouse_border_left or mx > mouse_border_right:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-mouse_max_rel, min(mouse_max_rel, self.rel))
        self.angle += self.rel * mouse_sens * self.game.delta_time
    
    def update(self):
        self.movement()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)