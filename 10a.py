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
    counter += 1
    print(trenutna)

print((counter+1)//2)



