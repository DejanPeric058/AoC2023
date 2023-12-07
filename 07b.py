

with open("07.txt") as f:
    text = f.read()

commands = [(x.split()[0], int(x.split()[1])) for x in text.splitlines()]

class Card:

    def __init__(self, pattern: str):
        self.pattern : str = pattern
        self.order : int = self.define_order()
        self.alphabetic_order : int = self.define_alphabetic_order()
        self.skupni_order : int = self.order * (14**5) + self.alphabetic_order
       
    def define_order(self):
        '''Define order, 5ok is 7, high card is 1'''
        my_slovar = self.vrni_slovar()
        if 'J' in my_slovar.keys():
            j = my_slovar.pop('J')
            if j in [4,5]:
                return 7
        else:
            j = 0
        values = sorted(my_slovar.values(), reverse = True)
        if values[0] == 5:
            return 7
        elif values[0] == 4:
            if j == 1:
                return 7
            else:
                return 6
        elif values[0] == 3:
            if j == 2:
                return 7
            elif j == 1:
                return 6
            elif values[1] == 2:
                return 5
            else:
                return 4
        elif values[0] == 2:
            if j == 3:
                return 7
            elif j == 2:
                return 6
            elif values[1] == 2:
                if j == 1:
                    return 5
                else:
                    return 3
            else:
                if j == 1:
                    return 4
                else:
                    return 2
        else:
            if j == 3:
                return 6
            elif j == 2:
                return 4
            elif j == 1:
                return 2
            else:
                return 1

    def vrni_slovar(self):
        '''empty'''
        my_dict = {}
        for a in self.pattern:
            if a in my_dict.keys():
                my_dict[a] += 1
            else:
                my_dict[a] = 1
        return my_dict
    
    def define_alphabetic_order(self):
        dd = ['J', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
        o = 1
        for i, x in enumerate(self.pattern):
            o += dd.index(x) * (14**(4 - i))
        return o

novi_sez = []
for card, bet in commands:
    c = Card(card)
    novi_sez.append((c.skupni_order, bet))

novi_sez = sorted(novi_sez, reverse=True)
my_sum = 0
d = len(novi_sez)
for i, (_, b) in enumerate(novi_sez):
    my_sum += (d - i) * b

print(my_sum)
