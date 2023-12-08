
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
    
should_restart = True
trenutni = 'AAA'
koraki = 0
while should_restart:
    for smer in smeri:
        if trenutni == 'ZZZ':
            print(koraki)
            should_restart = False
            break
        trenutni = my_dict[trenutni][smer]
        koraki += 1



