from cell import Cell, TypeCell
import random
from enum import Enum


class Complexity(Enum):
    easy = (1,)
    medium = (2,)
    hard = 3


class Map:
    def __init__(self, complexity):
        if complexity == Complexity.easy:
            self.size_x, self.size_y, self.count_bomb = 10, 10, 10
        elif complexity == Complexity.medium:
            self.size_x, self.size_y, self.count_bomb = 10, 10, 20
        else:
            self.size_x, self.size_y, self.count_bomb = 10, 10, 30

        self.cells = [[None for _ in range(self.size_x)] for _ in range(self.size_y)]
        self.randomFillMap()
        # self.FillCountBombOutside()

    def randomFillMap(self):
        for i in range(self.size_y):
            for j in range(self.size_x):
                self.cells[i][j] = Cell()

        current_count_bomb = 0
        while current_count_bomb < self.count_bomb:
            index_x = random.randint(0, self.size_x - 1)
            index_y = random.randint(0, self.size_y - 1)
            if self.cells[index_x][index_y].type == TypeCell.bomb:
                continue
            else:
                self.cells[index_x][index_y].type = TypeCell.bomb
                current_count_bomb += 1

    def FillCountBombOutside(self):
        result = 0
        for x in range(self.size_x):
            for y in range(self.size_y):
                if self.cells[x][y].type == TypeCell.bomb:
                    continue

                if x - 1 >= 0 and y - 1 >= 0:
                    if self.cells[y - 1][x - 1].type == TypeCell.bomb:
                        result += 1
                if y - 1 >= 0:
                    if self.cells[y - 1][x].type == TypeCell.bomb:
                        result += 1
                if x + 1 <= self.size_x - 1 and y - 1 >= 0:
                    if self.cells[y - 1][x + 1].type == TypeCell.bomb:
                        result += 1
                if x - 1 >= 0 and y + 1 <= self.size_y - 1:
                    if self.cells[y + 1][x - 1].type == TypeCell.bomb:
                        result += 1
                if y + 1 <= self.size_y - 1:
                    if self.cells[y + 1][x].type == TypeCell.bomb:
                        result += 1
                if x + 1 <= self.size_x - 1 and y + 1 <= self.size_y - 1:
                    if self.cells[y + 1][x + 1].type == TypeCell.bomb:
                        result += 1
                if x - 1 >= 0:
                    if self.cells[y][x - 1].type == TypeCell.bomb:
                        result += 1
                if x + 1 <= self.size_x - 1:
                    if self.cells[y][x + 1].type == TypeCell.bomb:
                        result += 1

                if result == 0:
                    self.cells[y][x].type = TypeCell.empty
                else:
                    self.cells[y][x].value = result
                    self.cells[y][x].type = TypeCell.number
