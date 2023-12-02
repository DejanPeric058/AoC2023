import numpy as np
with open("02.txt") as f:
    text = f.read()

commands = text.splitlines()
my_sum = 0

for i, command in enumerate(commands, start=1):
    parts = (command.split(': ')[1]).split('; ')
    colours = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }
    for part in parts:
        for cubes in part.split(', '):
            no, color = cubes.split(' ')
            colours[color] = max(int(no), colours[color]) 
    my_sum += np.prod(list(colours.values()))

print(my_sum)