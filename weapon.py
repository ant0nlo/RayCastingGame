import pygame as pg
from collections import deque
from time import time
from constants import *

class Weapon:
    def __init__(self, game, path='images/sprites/weapon/pistol/0.png', scale=0.4, animation_time=100):
        self.game = game
        self.scale = scale
        self.animation_time = animation_time
        self.images = self.load_images(path)
        self.image = self.images[0]
        self.weapon_pos = (HALF_WIDTH - self.image.get_width() // 2, HEIGHT - self.image.get_height())
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 50
        self.last_update_time = time()

    def load_images(self, path):
        image = pg.image.load(path).convert_alpha()
        image = pg.transform.smoothscale(image, (image.get_width() * self.scale* 8, image.get_height() * self.scale* 8))
        images = deque([image])
        for i in range(1, 4):  
            img_path = path.replace('0.png', f'{i}.png')
            try:
                img = pg.image.load(img_path).convert_alpha()
                img = pg.transform.smoothscale(img, (img.get_width() * self.scale * 8, img.get_height() * self.scale* 8))
                images.append(img)
            except FileNotFoundError:
                break
        return images

    def check_animation_time(self):
        current_time = time()
        if current_time - self.last_update_time >= self.animation_time / 1000:
            self.animation_trigger = True
            self.last_update_time = current_time
        else:
            self.animation_trigger = False

    def animate_shot(self):
        if self.reloading:
            self.game.hero.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        self.check_animation_time()
        self.animate_shot()
