import pygame


class Matrix:
    def __init__(self, size, dimension):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.neighbours = [[0 for _ in range(size)] for _ in range(size)]
        self.dimension = dimension
        self.remove_only = False
        self.add_only = False
        self.game = False

    def add_block(self, pos):
        x = pos[0] * self.size // self.dimension
        y = pos[1] * self.size // self.dimension

        if self.remove_only:
            self.grid[x][y] = 0
        elif self.add_only:
            self.grid[x][y] = 1
        else:
            self.grid[x][y] = 1 - self.grid[x][y]

    def draw_grid(self, window):
        for x in range(1, self.size + 1):
            pygame.draw.line(window, (255, 255, 255), (0, x * self.dimension / self.size), (self.dimension, x * self.dimension / self.size))
            pygame.draw.line(window, (255, 255, 255), (x * self.dimension / self.size, 0), (x * self.dimension / self.size, self.dimension))
            
    def draw_blocks(self, window):
        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y]:
                    pygame.draw.rect(window, (255, 255, 255), (x / self.size * self.dimension, y / self.size * self.dimension, self.dimension / self.size, self.dimension / self.size))

    def count_neighbours(self):
        for x in range(self.size):
            for y in range(self.size):
                c = 0
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        try:
                            c += self.grid[x + a][y + b]
                        except IndexError:
                            pass
                self.neighbours[x][y] = c - self.grid[x][y]

    def game_of_life(self):
        self.count_neighbours()
        for x in range(self.size):
            for y in range(self.size):
                if self.neighbours[x][y] not in [2, 3] and self.grid[x][y]:
                    self.grid[x][y] = 0
                if self.neighbours[x][y] == 3 and not self.grid[x][y]:
                    self.grid[x][y] = 1




