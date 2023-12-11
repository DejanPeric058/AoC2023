import numpy as np
with open("11.txt") as f:
    text = f.read()

commands = [[x for x in command] for command in text.splitlines()]
new_commands = []
for command in commands:
    new_commands.append(command)
    if "#" not in command:
        new_commands.append(command)
za_zamenjat = []
for j in range(len(new_commands[0])):
    vstavi_novo = True
    for i in range(len(new_commands)):
        if new_commands[i][j] =='#':
            vstavi_novo = False
    if vstavi_novo:
        za_zamenjat.append(j)
newer_commands = []
for command in new_commands:
    new_command = []
    for k,a in enumerate(command):
        new_command.append(a)
        if k in za_zamenjat:
            new_command.append(a)
    newer_commands.append(new_command)


def findall(element, matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                result.append((i, j))
    return result
my_sum = 0
lojtre = findall('#', newer_commands)
for i, (a,b) in enumerate(lojtre):
    for (c,d) in lojtre[i + 1:]:
        my_sum += np.abs(a-c) + np.abs(b-d)

print(my_sum)
