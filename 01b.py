cifre = '123456789'

with open ('01.txt') as f:
    text = f.read()

ukazi = text.splitlines()

my_sum = 0

words = {
    'one':1,
    'two':2,
    'three':3, 
    'four':4, 
    'five':5, 
    'six': 6, 
    'seven': 7,
    'eight': 8, 
    'nine': 9
        }

for ukaz in ukazi:
    vmesni = []
    for i, x in enumerate(ukaz):
        if x in cifre:
            vmesni.append(int(x))
        for word in words.keys():
            a = ukaz[i:].find(word)
            if a == 0:
                vmesni.append(words[word])
    vsota = vmesni[0] * 10 + vmesni[-1]
    my_sum += vsota
print(my_sum)