import numpy
import re
cifre = '1234567890'
with open("03.txt") as f:
    text =f.read()

commands = text.splitlines()
my_sum = 0

signals = [[k for k in row] for row in commands]
gear_dict = {}
vrednost = 0
vrednosti = []
sirina = len(signals)
for i, row in enumerate(signals):
    for j, x in enumerate(row):
        if x == '*':
            gear_dict[(i,j)] = []
        if x in cifre:
            vrednost = 10 * vrednost + int(x)

        
        elif vrednost != 0:
            m = j
            if j == 0:
                i = i-1
                j = sirina
            kji = []
            for k in range(j - len(str(vrednost)), j):
                signals[i][k] = vrednost
                kji.append((i,k))
                kji.append((i-1,k))
                kji.append((i+1,k))
            kji.append((i,j))
            kji.append((i-1,j))
            kji.append((i+1,j))
            kji.append((i,j - len(str(vrednost))-1))
            kji.append((i-1,j - len(str(vrednost))-1))
            kji.append((i+1,j - len(str(vrednost))-1))
            vrednosti.append([vrednost, kji])
            vrednost = 0
            if m != j:
                j = m
                i = i+1
        else:
            pass

for gear, gear_items in gear_dict.items():
    for cifra, pojavitve in vrednosti:
        if gear in pojavitve:
            gear_items.append(cifra)
    if len(gear_items) == 2:
        my_sum += gear_items[0] * gear_items[1]

print(my_sum)