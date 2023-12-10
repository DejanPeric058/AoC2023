import numpy as np
with open("10.txt") as f:
    text = f.read()

commands = text.splitlines()
my_map = [['.'] + [niz for niz in command] + ['.'] for command in commands]
my_map = [['.' for _ in range(len(my_map[0]))]] + my_map + [['.' for _ in range(len(my_map[0]))]]

def find_S(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'S':
                return (i, j)
            
i_s, j_s = find_S(my_map)
coordinates = [((i_s, j_s), 'S')]
if my_map[i_s - 1][j_s] in 'F|7':
    start = 'u'
    trenutna = my_map[i_s - 1][j_s]
elif my_map[i_s + 1][j_s] in 'J|L':
    start = 'd'
    trenutna = my_map[i_s + 1][j_s]
elif my_map[i_s][j_s + 1] in 'J-7':
    start = 'r'
    trenutna = my_map[i_s][j_s + 1]
elif my_map[i_s][j_s - 1] in 'LF-':
    start = 'l'
    trenutna = my_map[i_s][j_s - 1]
coordinates = [((i_s, j_s), 'S', start)]
counter = 0
while trenutna != 'S':
    if trenutna == 'F':
        if start == 'u':
            i_s, j_s = i_s, j_s + 1
            start = 'r'
            trenutna = my_map[i_s][j_s]
        elif start == 'l':
            i_s, j_s = i_s + 1, j_s
            start = 'd'
            trenutna = my_map[i_s][j_s]
    elif trenutna == 'L':
        if start == 'd':
            i_s, j_s = i_s, j_s + 1
            start = 'r'
            trenutna = my_map[i_s][j_s]
        elif start == 'l':
            i_s, j_s = i_s - 1, j_s
            start = 'u'
            trenutna = my_map[i_s][j_s]
    elif trenutna == 'J':
        if start == 'd':
            i_s, j_s = i_s, j_s - 1
            start = 'l'
            trenutna = my_map[i_s][j_s]
        elif start == 'r':
            i_s, j_s = i_s - 1, j_s
            start = 'u'
            trenutna = my_map[i_s][j_s]
    elif trenutna == '7':
        if start == 'u':
            i_s, j_s = i_s, j_s - 1
            start = 'l'
            trenutna = my_map[i_s][j_s]
        elif start == 'r':
            i_s, j_s = i_s + 1, j_s
            start = 'd'
            trenutna = my_map[i_s][j_s]
    elif trenutna == '|':
        if start == 'u':
            i_s, j_s = i_s - 1, j_s
            start = 'u'
            trenutna = my_map[i_s][j_s]
        elif start == 'd':
            i_s, j_s = i_s + 1, j_s
            start = 'd'
            trenutna = my_map[i_s][j_s]
    elif trenutna == '-':
        if start == 'l':
            i_s, j_s = i_s, j_s - 1
            start = 'l'
            trenutna = my_map[i_s][j_s]
        elif start == 'r':
            i_s, j_s = i_s, j_s + 1
            start = 'r'
            trenutna = my_map[i_s][j_s]
    coordinates.append(((i_s, j_s), trenutna, start))

    counter += 1

tiles1 = set()

testna = [[' ' for _ in range(len(my_map[0]))] for _ in range(len(my_map))]
for (x,y), s, _ in coordinates:
    testna[x][y] = s

for (x,y), s, smer in coordinates:
    if s == '|':
        if smer == 'd':
            for h in range(1, 500):
                tile = testna[x][y+h]
                if tile in 'LJF7|-S':
                    break
                else:
                    tiles1.add((x,y+h))
        elif smer == 'u':
            for h in range(1, 500):
                tile = testna[x][y-h]
                if tile in 'LJF7|-S':
                    break
                else:
                    tiles1.add((x,y-h))
    elif s == '-':
        if smer == 'l':
            for h in range(1, 500):
                tile = testna[x+h][y]
                if tile in 'LJF7|-S':
                    break
                else:
                    tiles1.add((x+h,y))
        elif smer == 'r':
            for h in range(1, 500):
                tile = testna[x-h][y]
                if tile in 'LJF7|-S':
                    break
                else:
                    tiles1.add((x-h,y))
    elif s == 'L':
        if smer == 'l':
            for h in range(1, 500):
                tile = testna[x][y-h]
                if tile in 'LJF7|-S':
                    break
                else:
                    tiles1.add((x,y-h))
            for h in range(1, 500):
                tile = testna[x+h][y]
                if tile in 'LJF7|-S':
                    break
                else:
                    tiles1.add((x+h,y))
    elif s == 'J':
        if smer == 'd':
            for h in range(1, 500):
                tile = testna[x+h][y]
                if tile in 'LJF7|-S':
                    break
                else:
                    tiles1.add((x+h,y))
            for h in range(1, 500):
                tile = testna[x][y+h]
                if tile in 'LJF7|-S':
                    break
                else:
                    tiles1.add((x,y+h))
    elif s == '7':
        if smer == 'r':
            for h in range(1, 500):
                tile = testna[x-h][y]
                if tile in 'LJF7|-S':
                    break
                else:
                    tiles1.add((x-h,y))
            for h in range(1, 500):
                tile = testna[x][y+h]
                if tile in 'LJF7|-S':
                    break
                else:
                    tiles1.add((x,y+h))
    elif s == 'F':
        if smer == 'u':
            for h in range(1, 500):
                tile = testna[x-h][y]
                if tile in 'LJF7|-S':
                    break
                else:
                    tiles1.add((x-h,y))
            for h in range(1, 500):
                tile = testna[x][y-h]
                if tile in 'LJF7|-S':
                    break
                else:
                    tiles1.add((x,y-h))

print(len(tiles1))
for (x,y) in list(tiles1):
    testna[x][y] = '*'
izpis = ''
for row in testna:
    izpis += ''.join(row)
    izpis += '\n'
print(izpis)

#for (x,y), s, smer in coordinates:
#    if s == '|':
#        if smer == 'u':
#            for h in range(1, 500):
#                tile = testna[x][y+h]
#                if tile in 'LJF7|-S':
#                    break
#                else:
#                    tiles1.add((x,y+h))
#        elif smer == 'd':
#            for h in range(1, 500):
#                tile = testna[x][y-h]
#                if tile in 'LJF7|-S':
#                    break
#                else:
#                    tiles1.add((x,y-h))
#    elif s == '-':
#        if smer == 'r':
#            for h in range(1, 500):
#                tile = testna[x+h][y]
#                if tile in 'LJF7|-S':
#                    break
#                else:
#                    tiles1.add((x+h,y))
#        elif smer == 'l':
#            for h in range(1, 500):
#                tile = testna[x-h][y]
#                if tile in 'LJF7|-S':
#                    break
#                else:
#                    tiles1.add((x-h,y))
#    elif s == 'L':
#        if smer == 'd':
#            for h in range(1, 500):
#                tile = testna[x][y-h]
#                if tile in 'LJF7|-S':
#                    break
#                else:
#                    tiles1.add((x,y-h))
#            for h in range(1, 500):
#                tile = testna[x+h][y]
#                if tile in 'LJF7|-S':
#                    break
#                else:
#                    tiles1.add((x+h,y))
#    elif s == 'J':
#        if smer == 'r':
#            for h in range(1, 500):
#                tile = testna[x+h][y]
#                if tile in 'LJF7|-S':
#                    break
#                else:
#                    tiles1.add((x+h,y))
#            for h in range(1, 500):
#                tile = testna[x][y+h]
#                if tile in 'LJF7|-S':
#                    break
#                else:
#                    tiles1.add((x,y+h))
#    elif s == '7':
#        if smer == 'u':
#            for h in range(1, 500):
#                tile = testna[x-h][y]
#                if tile in 'LJF7|-S':
#                    break
#                else:
#                    tiles1.add((x-h,y))
#            for h in range(1, 500):
#                tile = testna[x][y+h]
#                if tile in 'LJF7|-S':
#                    break
#                else:
#                    tiles1.add((x,y+h))
#    elif s == 'F':
#        if smer == 'l':
#            for h in range(1, 500):
#                tile = testna[x-h][y]
#                if tile in 'LJF7|-S':
#                    break
#                else:
#                    tiles1.add((x-h,y))
#            for h in range(1, 500):
#                tile = testna[x][y-h]
#                if tile in 'LJF7|-S':
#                    break
#                else:
#                    tiles1.add((x,y-h))
#
#print(len(tiles1))
#for (x,y) in list(tiles1):
#    testna[x][y] = '*'
#izpis = ''
#for row in testna:
#    izpis += ''.join(row)
#    izpis += '\n'
#print(izpis)