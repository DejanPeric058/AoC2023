cifre = '123456789'

with open ('01.txt') as f:
    text = f.read()

ukazi = text.splitlines()

my_sum = 0

for ukaz in ukazi:
    vmesni = []
    for x in ukaz:
        if x in cifre:
            vmesni.append(int(x))
    vsota = vmesni[0] * 10 + vmesni[-1]
    my_sum += vsota
print(my_sum)