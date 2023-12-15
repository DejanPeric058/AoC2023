
with open("15.txt") as f:
    text = f.read()

commands = text.split(',')

def calculate_hash(previous, input):
    return ((previous + ord(input)) * 17) % 256

count = 0

for command in commands:
    y = 0
    for char in command:
        y = calculate_hash(y, char)
    count += y

print(count)
