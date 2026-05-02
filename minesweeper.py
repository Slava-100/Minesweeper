import random

def randomFillMap(size_x, size_y, count_bomb, map):
    for i in range(size_y):
        map.append([])
        for j in range(size_x):
            map[i].append("*")
    
    current_count_bomb = 0
    while current_count_bomb < count_bomb:
        index_x = random.randint(0, 19)
        index_y = random.randint(0, 19)
        if map[index_x][index_y] == "B":
            continue
        else:       
           map[index_x][index_y] = "B"
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

size_x = 20
size_y = 20
count_bomb = 20
map = []

randomFillMap(size_x, size_y, count_bomb, map)

for i in range(size_y):
    for j in range(size_x):
        print(map[i][j], end = ' ')
    print()

x = 1 
while x != -1:    
    x = int(input("x:"))
    y = int(input("y:"))
    FillCountBombOutside(x, y, map)

    for i in range(size_y):
        for j in range(size_x):
            print(map[i][j], end = ' ')
        print()