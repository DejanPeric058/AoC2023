import numpy as np
with open("14.txt") as f:
    text = f.read()

commands = [[x for x in command] for command in text.splitlines()]
commands = [[commands[j][i] for j in range (len (commands))] for i in range (len (commands[0]))]

for i, command in enumerate(commands):
    stable = -1
    for j, stone in enumerate(command):
        if stone == '#':
            stable = j
        elif stone == 'O':
            commands[i][stable + 1] = 'O'
            if j != stable + 1:
                commands[i][j] = '.'
            stable += 1

commands = [[commands[j][i] for j in range (len (commands))] for i in range (len (commands[0]))]
n = len(commands)
count = 0
for i, command in enumerate(commands):
    count += command.count('O') * (n - i)

print(count)
