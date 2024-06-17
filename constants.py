import math
import pygame as pg

res = WIDTH, HEIGHT = 1600, 900
fps = 60 
screen = pg.display.set_mode(res, pg.FULLSCREEN)

HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

hero_positions = 1.5, 5
hero_angle = 0
hero_speed = 0.004

hero_size = 50
hero_max_helth = 1000

mouse_sens = 0.0003
mouse_max_rel = 40
mouse_border_left = 100
mouse_border_right = WIDTH - mouse_border_left

FOV = math.pi/3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2

FLOOR_COLOR = (91,84,71)
