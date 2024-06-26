import pygame as pg

map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 3, 3, 3, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 3, 0, 3, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 3, 0, 0, 3, 1, 1, 1],
    [1, 3, 3, 3, 3, 0, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3],
    [1, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 3, 3, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 3, 0, 0, 0, 3, 3, 3, 3, 0, 3, 3, 0, 3],
    [3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3],
    [3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 3, 0, 3],
    [1, 0, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3],
    [1, 0, 0, 0, 0, 0, 3, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4],
    [4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 4, 4, 4],
    [4, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 4, 0, 0, 4, 4, 4, 0, 4, 4, 0, 4, 0, 4],
    [4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 4, 4, 0, 4, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.map = map
        self.world_map = {}
        self.rows = len(self.map)
        self.cols = len(self.map[0])
        self.get_map()

    def get_map(self):
        for j in range(len(self.map)):
            row = self.map[j]
            for i in range(len(row)):
                value = row[i]
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        for pos in self.world_map:
            x = pos[0] * 100
            y = pos[1] * 100
            width = 100
            height = 100
            color = 'black'
            line_width = 2
            pg.draw.rect(self.game.screen, color, (x, y, width, height), line_width)

        