from cell import Cell, TypeCell
import random
from enum import Enum
from state_play import StatePlay

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

        self.cells = []
        self.randomFillMap()
        self.FillCountBombOutside()

    def randomFillMap(self):
        self.cells = [[None for _ in range(self.size_x)] for _ in range(self.size_y)]
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
                if self.cells[y][x].type == TypeCell.bomb:
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
                result = 0
    
    def openeed(self):
        countFlag = 0
        for x in range(self.size_x):
            for y in range(self.size_y):
                if self.cells[y][x].type != TypeCell.number:
                    continue

                if x - 1 >= 0 and y - 1 >= 0:
                    if self.cells[y - 1][x - 1].type == TypeCell.flag:
                        countFlag += 1
                if y - 1 >= 0:
                    if self.cells[y - 1][x].type == TypeCell.flag:
                        countFlag += 1
                if x + 1 <= self.size_x - 1 and y - 1 >= 0:
                    if self.cells[y - 1][x + 1].type == TypeCell.flag:
                        countFlag += 1
                if x - 1 >= 0 and y + 1 <= self.size_y - 1:
                    if self.cells[y + 1][x - 1].type == TypeCell.flag:
                        countFlag += 1
                if y + 1 <= self.size_y - 1:
                    if self.cells[y + 1][x].type == TypeCell.flag:
                        countFlag += 1
                if x + 1 <= self.size_x - 1 and y + 1 <= self.size_y - 1:
                    if self.cells[y + 1][x + 1].type == TypeCell.flag:
                        countFlag += 1
                if x - 1 >= 0:
                    if self.cells[y][x - 1].type == TypeCell.flag:
                        countFlag += 1
                if x + 1 <= self.size_x - 1:
                    if self.cells[y][x + 1].type == TypeCell.flag:
                        countFlag += 1
                
                if countFlag != self.cells[y][x]:
                    continue
                else:
                    if x - 1 >= 0 and y - 1 >= 0:
                        if self.cells[y - 1][x - 1].isOpen == False:
                            self.play(x, y)
                    if y - 1 >= 0:
                        if self.cells[y - 1][x].isOpen == False:
                            self.play(x, y)
                    if x + 1 <= self.size_x - 1 and y - 1 >= 0:
                        if self.cells[y - 1][x + 1].isOpen == False:
                            self.play(x, y)
                    if x - 1 >= 0 and y + 1 <= self.size_y - 1:
                        if self.cells[y + 1][x - 1].isOpen == False:
                            self.play(x, y)
                    if y + 1 <= self.size_y - 1:
                        if self.cells[y + 1][x].isOpen == False:
                            self.play(x, y)
                    if x + 1 <= self.size_x - 1 and y + 1 <= self.size_y - 1:
                        if self.cells[y + 1][x + 1].isOpen == False:
                            self.play(x, y)
                    if x - 1 >= 0:
                        if self.cells[y][x - 1].isOpen == False:
                            self.play(x, y)
                    if x + 1 <= self.size_x - 1:
                        if self.cells[y][x + 1].isOpen == False:
                            self.play(x, y)
        return
                                
    def showMap(self):
          for row in self.cells:
              for cell in row:
                  if cell.isOpen == True:
                      if cell.type == TypeCell.number:
                          print(cell.value, end=" ")
                      elif cell.type == TypeCell.flag:
                          print("!", end=" ")
                      else:
                          print(" ", end=" ")
                  else:
                      print("*", end=" ")
              print()     
                    
    def play(self, index_x, index_y, state_play = StatePlay.default):
        if index_x >= self.size_x or index_x < 0:
            return
        if index_y >= self.size_y or index_y < 0:
            return
    
        if state_play == StatePlay.flag:
            if self.cells[index_y][index_x].type == TypeCell.flag:
                self.cells[index_y][index_x].isOpen = False
                self.cells[index_y][index_x].type = TypeCell.empty
            else:
                if self.cells[index_y][index_x].isOpen == False:
                    self.cells[index_y][index_x].isOpen = True
                    self.cells[index_y][index_x].type = TypeCell.flag
            return
        
        if self.cells[index_y][index_x].isOpen == True:
            return
        
        if self.cells[index_y][index_x].type == TypeCell.number:
            self.cells[index_y][index_x].isOpen = True
        
        if self.cells[index_y][index_x].type == TypeCell.bomb:
            self.cells[index_y][index_x].isOpen = True
            print("Ой, ты попал в бомбу!")
            input("")
            self.randomFillMap()
            self.FillCountBombOutside()
            return

        if self.cells[index_y][index_x].type == TypeCell.empty:
            self.playIsEmpty(index_x, index_y)
            return
    
    def playIsEmpty(self, index_x, index_y):
        self.cells[index_y][index_x].isOpen = True
        self.play(index_x-1, index_y)       
        self.play(index_x-1, index_y-1)                      
        self.play(index_x, index_y-1)
        self.play(index_x+1, index_y-1)
        self.play(index_x+1, index_y)
        self.play(index_x+1, index_y+1)
        self.play(index_x, index_y+1)
        self.play(index_x-1, index_y+1)