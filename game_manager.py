from random import choices, randrange
from constants import *
from enemy import *

class GameManager:
    def __init__(self, game):
        self.game = game
        self.npc_list = []
        self.npc_sprite_path = 'images/sprites/npc/'
        self.npc_positions = {}

        self.enemies = 20
        self.npc_types = [Skeleton, Demon]
        self.weights = [50, 30]
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        self.spawn_npc()

    def check_win(self):
        if not len(self.npc_positions):
            self.game.objects.win()
            pg.display.flip()

    def spawn_npc(self):
        for i in range(self.enemies):
                npc = choices(self.npc_types, self.weights)[0]
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                    pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [npc.update() for npc in self.npc_list]
        self.check_win()
        self.enemy_count()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def enemy_count(self):
        live_enemies = sum(1 for npc in self.npc_list if npc.alive)
        font = pg.font.Font(None, 36)
        text = font.render(f'Enemies: {live_enemies}', True, (133, 0, 0))
        text_rect = text.get_rect(midtop=(WIDTH // 2, 20))
        self.game.screen.blit(text, text_rect)