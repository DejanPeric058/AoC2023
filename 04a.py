
with open("04.txt") as f:
    text = f.read()

commands = text.splitlines()
my_sum = 0
for command in commands:
    parts = (command.split(': ')[1]).split(' | ')
    dobitne, moje = parts[0].split(' '), parts[1].split(' ')
    while '' in dobitne:
        dobitne.remove('')
    while '' in moje:
        moje.remove('')

    dobitne, moje = set(dobitne), set(moje)
    
    i = len(dobitne.intersection(moje))
    if i != 0:
        my_sum += 2**(i-1)

print(my_sum)