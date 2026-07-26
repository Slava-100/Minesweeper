from map import Map
from cell import TypeCell
from enum import Enum
from state_play import StatePlay

class Minesweeper:
    def __init__(self, complexity):
        self.state_play = StatePlay.default
        self.game_map = Map(complexity)
        self.start()

    def start(self):
        end = False 
        while end == False:
            self.game_map.showMap()    
            if self.state_play == StatePlay.default:
                xy = input("(Обычный ход) Введи координаты хода (x y):")
            else:
                xy = input("(Флаг) Введи координаты хода (x y):")
            
            if xy == "*":
                if self.state_play == StatePlay.flag:
                    self.state_play = StatePlay.default 
                else:
                    self.state_play = StatePlay.flag
            elif xy == "**":
                self.game_map.openeed()
            else:
                xy_array = xy.strip().split()
                x = int(xy_array[0])
                y = int(xy_array[1])
                self.game_map.play(x, y, self.state_play)   
                

    
