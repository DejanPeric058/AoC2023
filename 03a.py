import re
cifre = '0123456789'

with open("03.txt") as f:
    text =f.read()



commands = text.splitlines()
my_sum = 0
dolzina, sirina = len(commands), len(commands[0])
for i, command in enumerate(commands):
    indeksi = []
    sez = re.split(r'\D+', command)
    for s in sez:
        
        if len(s) > 0:
            
            mnozica = set()
            
            prvi_ind = command.find(s)
            if indeksi:
                prvi_ind = indeksi[-1] + command[indeksi[-1]:].find(s)
            indeksi.append(prvi_ind)
            zadnji_ind = prvi_ind + len(s)
            if prvi_ind >= 0:
                mnozica.add(command[prvi_ind-1])
            if zadnji_ind  < sirina:
                mnozica.add(command[zadnji_ind])
            for j in range(max(prvi_ind-1,0),min(zadnji_ind+1,sirina)):
                if i != 0:
                    mnozica.add(commands[i-1][j])
                if i +1 != dolzina:
                    mnozica.add(commands[i+1][j])
            if len(mnozica) != 1:
                my_sum += int(s)
                
                print(mnozica)
                print(s)
            else:
                pass #print(s)

print(my_sum)