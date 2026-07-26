from map import Complexity
from minesweeper import Minesweeper

isCorrectly = False
while isCorrectly == False:
    complexity = input("Выбери сложность игры: easy, medium, hard:")
    if complexity == "easy":
        minesweeper = Minesweeper(Complexity.easy)
        isCorrectly = True
    elif complexity == "medium":
        minesweeper = Minesweeper(Complexity.medium)
        isCorrectly = True
    elif complexity == "hard":
        minesweeper = Minesweeper(Complexity.hard)
        isCorrectly = True
    else:
        print("ТАКОГО УРОВНЯ ИГРЫ НЕ СУЩЕСТВУЕТ!!! ОПАСНО ДЛЯ ЖИЗНИ!!!")