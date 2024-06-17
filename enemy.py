import pygame as pg
from constants import *
from sprite import *
from random import randint, random

class NPC(Sprite):
    def __init__(self, game, path='images/sprites/npc/skeleton/0.png', pos=(10.5, 5.5),
                 scale=0.6, shift=0.38, animation_time=180):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_images = self.get_images(self.path + '/attack')
        self.death_images = self.get_images(self.path + '/death')
        self.pain_images = self.get_images(self.path + '/pain')
        self.walk_images = self.get_images(self.path + '/walk')

        self.size = 20
        self.frame_counter = 0
        self.alive = True
        self.pain = False
        self.ray_cast_value = False
        self.hero_search_trigger = False
        self.death_time = None
        self.blink_time = None
        self.blinking = False 

    def update(self):
        self.check_animation_time()
        self.get_sprite()
        self.run_logic()

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx * self.size), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * self.size)):
            self.y += dy
    
    def movement(self):
        next_pos = self.game.pathfinding.get_path(self.map_pos, self.game.hero.map_pos)
        next_x, next_y = next_pos

        # pg.draw.rect(self.game.screen, 'blue', (100 * next_x, 100 * next_y, 100, 100))
        if next_pos not in self.game.manager.npc_positions:
            angle = math.atan2(next_y + 0.5 - self.y, next_x + 0.5 - self.x)
            dx = math.cos(angle) * self.speed
            dy = math.sin(angle) * self.speed
            self.check_wall_collision(dx, dy)


    def attack(self):
        if self.animation_trigger:
            if random() < self.accuracy:
                self.game.hero.get_damage(self.attack_damage)

    def animate_death(self):
        if not self.alive:
             if self.frame_counter < len(self.death_images) - 1:
                if self.animation_trigger:
                    self.death_images.rotate(-1)
                    self.image = self.death_images[0]
                    self.frame_counter += 1
             else:
                 if self.death_time is None:
                    self.death_time = pg.time.get_ticks()  
                 if pg.time.get_ticks() - self.death_time > 2000: 
                    if self.blink_time is None:
                        self.blink_time = pg.time.get_ticks()
                    if pg.time.get_ticks() - self.blink_time > 200: 
                        self.blink_time = pg.time.get_ticks()
                        self.blinking = not self.blinking  
                    if pg.time.get_ticks() - self.death_time > 4000: 
                        self.image = None
                    else:
                        self.image = self.death_images[0] if self.blinking else None 


    def animate_pain(self):
        self.animate(self.pain_images)
        if self.animation_trigger:
            self.pain = False

    def check_hit_in_npc(self):
        if self.ray_cast_value and self.game.hero.shot:
            if HALF_WIDTH - self.sprite_half_width < self.screen_x < HALF_WIDTH + self.sprite_half_width:
                self.game.hero.shot = False
                self.pain = True
                self.health -= self.game.weapon.damage
                self.check_health()

    def check_health(self):
        if self.health < 1:
            self.alive = False

    def run_logic(self):
        if self.alive:
            self.ray_cast_value = self.ray_cast_hero_npc()
            self.check_hit_in_npc()

            if self.pain:
                self.animate_pain()

            elif self.ray_cast_value:
                self.hero_search_trigger = True

                if self.dist < self.attack_dist:
                    self.animate(self.attack_images)
                    self.attack()
                else:
                    self.animate(self.walk_images)
                    self.movement()

            elif self.hero_search_trigger:
                self.animate(self.walk_images)
                self.movement()

            else:
                self.animate(self.walk_images)
        else:
            self.animate_death()

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

    def ray_cast_hero_npc(self):
        if self.game.hero.map_pos == self.map_pos:
            return True

        wall_dist_v, wall_dist_h = 0, 0
        hero_dist_v, hero_dist_h = 0, 0

        ox, oy = self.game.hero.pos
        x_map, y_map = self.game.hero.map_pos

        ray_angle = self.theta

        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        # horizontals
        y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

        depth_hor = (y_hor - oy) / sin_a
        x_hor = ox + depth_hor * cos_a

        delta_depth = dy / sin_a
        dx = delta_depth * cos_a

        for i in range(MAX_DEPTH):
            tile_hor = int(x_hor), int(y_hor)
            if tile_hor == self.map_pos:
                hero_dist_h = depth_hor
                break
            if tile_hor in self.game.map.world_map:
                wall_dist_h = depth_hor
                break
            x_hor += dx
            y_hor += dy
            depth_hor += delta_depth

        # verticals
        x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

        depth_vert = (x_vert - ox) / cos_a
        y_vert = oy + depth_vert * sin_a

        delta_depth = dx / cos_a
        dy = delta_depth * sin_a

        for i in range(MAX_DEPTH):
            tile_vert = int(x_vert), int(y_vert)
            if tile_vert == self.map_pos:
                hero_dist_v = depth_vert
                break
            if tile_vert in self.game.map.world_map:
                wall_dist_v = depth_vert
                break
            x_vert += dx
            y_vert += dy
            depth_vert += delta_depth

        hero_dist = max(hero_dist_v, hero_dist_h)
        wall_dist = max(wall_dist_v, wall_dist_h)

        if 0 < hero_dist < wall_dist or not wall_dist:
            return True
        return False


class Skeleton(NPC):
    def __init__(self, game, path='images/sprites/npc/skeleton/0.png', pos=(10.5, 5.5),
                 scale=1, shift=0.25, animation_time=100):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_dist = 1.0
        self.health = 100
        self.attack_damage = 10
        self.speed = 0.03
        self.accuracy = 0.15

class Demon(NPC):
    def __init__(self, game, path='images/sprites/npc/demon/0.png', pos=(10.5, 6.5),
                 scale=0.6, shift=0.3, animation_time=100):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_dist = 1.0
        self.health = 150
        self.attack_damage = 25
        self.speed = 0.02
        self.accuracy = 0.4

class Monster(NPC):
    def __init__(self, game, path='images/sprites/npc/bringer/0.png', pos=(11.5, 6.0),
                 scale=0.8, shift=0.05, animation_time=110):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_dist = 1.0
        self.health = 150
        self.attack_damage = 15
        self.speed = 0.03
        self.accuracy = 0.3
