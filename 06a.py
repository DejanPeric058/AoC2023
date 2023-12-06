with open("06.txt") as f:
    text = f.read()

commands = text.splitlines()
time = commands[0].split()[1:]
time = [int(j) for j in time]
distance = commands[1].split()[1:]
distance = [int(j) for j in distance]
my_product = 1
for cas, razdalja in zip(time, distance):
    my_count = 0
    for i in range(1,cas):
        if i * (cas - i) > razdalja:
            my_count += 1
    my_product *= my_count
print(my_product)