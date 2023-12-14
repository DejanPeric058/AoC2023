import numpy as np
with open("13.txt") as f:
    text = f.read()

commands = text.splitlines()
new_commands = []
add = []
for command in commands:
    if command == '':
        new_commands.append(add)
        add = []
    else:
        add.append(list(command))
new_commands.append(add)
commands = new_commands
count = 0

def simetrala_na_vrstici(matrix):
    dol = len(matrix)
    for x in range(1, dol):
        oddo = min(x, dol - x)
        y = matrix[x: x + oddo]
        y = y[::-1]
        if matrix[x - oddo: x] == y:
            return x
        
    return None

for command in commands:
    simetrala_vrstica = simetrala_na_vrstici(command)
    if simetrala_vrstica is not None:
        count += 100 * simetrala_vrstica
    else:
        result = [[command[j][i] for j in range (len (command))] for i in range (len (command[0]))]
        count += simetrala_na_vrstici(result)

print(count)
