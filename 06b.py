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

import numpy as np

t2 = [49877895]
s2 = [356137815021882]

rez = 1
for i in range(len(t2)):
    x1 = (-t2[i] + np.sqrt(t2[i] ** 2 - 4 * s2[i]))/ -2
    x2 = (-t2[i] - np.sqrt(t2[i] ** 2 - 4 * s2[i]))/ -2
    if x1 == np.ceil(x1):
        x1 += 0.01
        x1 = np.ceil(x1)
    if x2 == np.ceil(x2):
        x2 += 0.01
        x2 = np.ceil(x2)
    x1 = np.ceil(x1)
    x2 = np.floor(x2)
    print(x2, x1)
    print(x2 - x1 + 1)
    rez = rez * (x2 - x1 + 1)
    print(rez)