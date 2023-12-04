
with open("04.txt") as f:
    text = f.read()

commands = text.splitlines()
my_sum = 0
my_dict = { i: 1 for i in range(len(commands))}
for m, command in enumerate(commands):
    parts = (command.split(': ')[1]).split(' | ')
    dobitne, moje = parts[0].split(' '), parts[1].split(' ')
    while '' in dobitne:
        dobitne.remove('')
    while '' in moje:
        moje.remove('')

    dobitne, moje = set(dobitne), set(moje)
    
    i = len(dobitne.intersection(moje))
    
    if i != 0:
        for _ in range(my_dict[m]):
            for j in range(m+1, min(m + i + 1, len(commands))):
                my_dict[j] += 1
                

print(sum(my_dict.values()))