
with open("02.txt") as f:
    text = f.read()

commands = text.splitlines()
colours = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}
my_sum = 0

for i, command in enumerate(commands, start=1):
    parts = (command.split(': ')[1]).split('; ')
    possible = True
    for part in parts:
        for cubes in part.split(', '):
            no, color = cubes.split(' ')
            if int(no) > colours[color]:
                possible = False 
    if possible:
        my_sum += i

print(my_sum)