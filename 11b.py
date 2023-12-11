
with open("11.txt") as f:
    text = f.read()
VREDNOST = 1000000 - 1
commands = [[x for x in command] for command in text.splitlines()]
new_commands = []
vrstice = []
stolpci = []
for k, command in enumerate(commands):
    if "#" not in command:
        vrstice.append(k)
for j in range(len(commands[0])):
    vstavi_novo = True
    for i in range(len(commands)):
        if commands[i][j] =='#':
            vstavi_novo = False
    if vstavi_novo:
        stolpci.append(j)


def findall(element, matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                result.append((i, j))
    return result
my_sum = 0
lojtre = findall('#', commands)
for i, (a,b) in enumerate(lojtre):
    for (c,d) in lojtre[i + 1:]:
        x_delta, y_delta = max(a,c) - min(a,c), max(b,d) - min(b,d)
        my_sum += x_delta + y_delta
        for z in range(min(a,c), max(a,c)):
            if z in vrstice:
                my_sum += VREDNOST
        for z in range(min(b,d), max(b,d)):
            if z in stolpci:
                my_sum += VREDNOST

print(my_sum)
