with open("06.txt") as f:
    text = f.read()

commands = text.splitlines()
time = int(commands[0].split(':')[1].replace(' ', ''))
distance = int(commands[1].split(':')[1].replace(' ', ''))
my_count = 0
for i in range(1,time):
    if i * (time - i) > distance:
        my_count = (time - 1) - 2*(i-1)
        break
print(my_count)