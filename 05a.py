cifre = '1234567890'

with open("05.txt") as f:
    text = f.read()

commands = text.splitlines()
seeds = []
for x in commands[0].split(' ')[1:]:
    seeds.append(int(x))
vsebovanosti = []
for command in commands[2:]:
    if command == '':
        vsebovanosti.append(preveri)
    elif command[0] in cifre:
        start1, start2, my_range = command.split(' ')
        start1, start2, my_range = int(start1), int(start2), int(my_range)
        preveri.append(([start1, start2], my_range))
    else:
        preveri = []
vsebovanosti.append(preveri)

for vsebovanost in vsebovanosti:
    for poz, seed in enumerate(seeds):
        for pogoj in vsebovanost:
            where, how_many = pogoj
            s1, s2 = where
            if s2 <= seed < s2 + how_many:
                seeds[poz] = seed + (s1 - s2)
                break


print(min(seeds))