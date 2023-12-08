
with open('08.txt') as f:
    text = f.read()

commands = text.splitlines()
smeri = [x for x in commands[0]]
my_dict = {}

for command in commands[2:]:
    location, levo, desno = command[:3], command[7:10], command[12:15]
    my_dict[location] = {
        "L": levo,
        "R": desno
    }
    
starters = []
for location in my_dict.keys():
    if location[2] == 'A':
        starters.append(location)

all_koraki = []

for trenutni in starters:
    should_restart = True
    koraki = 0
    while should_restart:
        for smer in smeri:
            if trenutni[2] == 'Z':
                all_koraki.append(koraki)
                should_restart = False
                break
            trenutni = my_dict[trenutni][smer]
            koraki += 1

from math import gcd   #will work for an int array of any length
lcm = 1
for i in all_koraki:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)



