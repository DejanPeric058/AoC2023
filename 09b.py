import scipy.special as sp
with open("09.txt") as f:
    text = f.read()

commands = [[int(x) for x in command.split()] for command in text.splitlines()]
my_sum = 0
for command in commands:
    ekstropolant = 0
    n = len(command) - 1
    for i in range(n):
        ekstropolant += sp.comb(n, i+1)*((-1)**i) * command[i]
    my_sum += ekstropolant

print(my_sum)