import pygame as pg
from constants import *

class Objects:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.get_wall_textures()
        self.sky_image = self.get_texture('images/textures/sky3.png', (WIDTH, HALF_HEIGHT))
        self.blood_screen = self.get_texture('images/textures/hit.png', res)
        self.game_over_image = self.get_texture('images/textures/g_o.png', res)
        self.win_image = self.get_texture('images/textures/win3.png', res)
        self.sky_offset = 0
        
    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def win(self):
        self.screen.blit(self.win_image, (0, 0))

    def game_over(self):
        self.screen.blit(self.blood_screen, (0, 0))
        self.screen.blit(self.game_over_image, (0, 0))

    def hero_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.hero.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        def sort_key(obj):
            return obj[0]

        all_objects = sorted(self.game.raycasting.objects_to_render, key=sort_key, reverse=True)
        for depth, image, pos in all_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def get_wall_textures(self):
        return {
            1: self.get_texture('images/textures/w4.jpg'),
            2: self.get_texture('images/textures/w1.png'),
            3: self.get_texture('images/textures/w5.jpg'),
            4: self.get_texture('images/textures/w2.png'),
        }