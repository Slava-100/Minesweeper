import cell
import random
from enum import Enum

class Сomplexity(Enum):
    easy = 1,
    medium = 2,
    hard = 3
    
class Map:
    def __init__(self, complexity):
        if complexity == Сomplexity.easy:
            self.size_x = 10
            self.size_y = 10
            self.count_bomb = 10
        elif complexity == Сomplexity.medium:
            self.size_x = 10
            self.size_y = 10
            self.count_bomb = 20
        else:
            self.size_x = 10
            self.size_y = 10
            self.count_bomb = 30
            
        self.cells = [self.size_x][self.size_y]

    def randomFillMap(self):
        for i in range(self.size_y):
            for j in range(self.size_x):
                self.cells[i][j] = cell.Cell()
    
        current_count_bomb = 0
        while current_count_bomb < self.count_bomb:
            index_x = random.randint(0, 19)
            index_y = random.randint(0, 19)
            if self.cells[index_x][index_y] == "B":
                continue
            else:       
                self.cells[index_x][index_y] = "B"
                current_count_bomb += 1

        


def FillCountBombOutside(x, y, map):
    result = 0
    if x - 1 >= 0 and y - 1 >= 0:
        if map[y - 1][x - 1] == "B":
            result += 1
    if y - 1 >= 0:
        if map[y - 1][x] == "B":
            result += 1
    if x + 1 <= 19 and y - 1 >= 0:
        if map[y - 1][x + 1] == "B":
            result += 1
    if x - 1 >= 0 and y + 1 <= 19:
        if map[y + 1][x - 1] == "B":
            result += 1
    if y + 1 <= 19:
        if map[y + 1][x] == "B":
            result += 1
    if x + 1 <= 19 and y + 1 <= 19:
        if map[y + 1][x + 1] == "B":
            result += 1
    if x - 1 >= 0:
        if map[y][x - 1] == "B":
            result += 1
    if x + 1 <= 19:
        if map[y][x + 1] == "B":
            result += 1
    
    map[y][x] = result                  



for i in range(size_y):
    for j in range(size_x):
        print(map[i][j], end = ' ')
    print()

x = 1 
while x != -1:    
    x = int(input("x:"))
    y = int(input("y:"))
    map.FillCountBombOutside(x, y, map)

    for i in range(size_y):
        for j in range(size_x):
            print(map[i][j], end = ' ')
        print()
        