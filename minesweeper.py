from map import Map, Complexity
from cell import TypeCell

game_map = Map(Complexity.easy)

for row in game_map.cells:
    for cell in row:
        if cell.type == TypeCell.number:
            print(cell.value, end=" ")
        elif cell.type == TypeCell.bomb:
            print("B", end=" ")
        else:
            print(" ", end=" ")
    print()
