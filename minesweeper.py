from map import Map, Complexity
from cell import TypeCell

def showMap(game_map):
    for row in game_map.cells:
        for cell in row:
            if cell.isOpen == True:
                if cell.type == TypeCell.number:
                    print(cell.value, end=" ")
                else:
                    print(" ", end=" ")
            else:
                print("*", end=" ")
        print()

def game(game_map):
    end = False 
    while end == False:
        showMap(game_map)    
        xy = input("Введи координаты хода (x y):")
        xy_array = xy.strip().split()
        x = int(xy_array[0])
        y = int(xy_array[1])
        game_map.play(x, y)       

game_map = Map(Complexity.easy)
game(game_map)

