
with open("15.txt") as f:
    text = f.read()

commands = text.split(',')

def calculate_hash(previous, input):
    return ((previous + ord(input)) * 17) % 256

count = 0
my_dict = {i: [] for i in range(256)}

for command in commands:
    y = 0
    if '-' in command:
        a = command[:-1]
        for char in a:
            y = calculate_hash(y, char)
        for lenses, value in my_dict[y]:
            if lenses == a:
                my_dict[y].remove((lenses, value))
                break
    else:
        a, b = command.split('=')
        b = int(b)
        flag = True
        for char in a:
            y = calculate_hash(y, char)
        for j, (lenses, value) in enumerate(my_dict[y]):
            if lenses == a:
                my_dict[y][j] = (lenses, b)
                flag = False
                break
        if flag:
            my_dict[y].append((a, b))


for k, v in my_dict.items():
    for m, (_, value) in enumerate(v):
        count += (k + 1) * (m + 1) * value

print(count)
