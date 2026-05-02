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
           
size_x = 20
size_y = 20
count_bomb = 20
map = []

randomFillMap(size_x, size_y, count_bomb, map)

for i in range(size_y):
    for j in range(size_x):
        print(map[i][j], end = ' ')
    print()