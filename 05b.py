cifre = '1234567890'
# Code ran 2h.
with open("05.txt") as f:
    text = f.read()

commands = text.splitlines()
seeds = []
for i, x in enumerate(commands[0].split(' ')[1:]):
    if i % 2 == 0:
        y = x
    else:
        #print(y,x)
        seeds.append((int(y),int(x)))

def nivseedih(x, sez1):
    for range1 in sez1:
        a, b = range1
        if a - 1 < x < a + b:
            return False
    return True


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

location = -1
seed = 0
while nivseedih(seed, seeds):
    #if location % (10**7) == 0:
        #print(location)
    location += 1
    seed = location
    for vsebovanost in reversed(vsebovanosti):
        for pogoj in vsebovanost:
            where, how_many = pogoj
            s2, s1 = where
            if s2 <= seed < s2 + how_many:
                seed = seed + (s1 - s2)
                break
    


print(location)