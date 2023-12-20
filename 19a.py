import pprint 
pp = pprint.PrettyPrinter(indent=4)

with open("19.txt") as f:
    text = f.read()

commands = text.splitlines()
workflows = []
parts = []
flag = False
for command in commands:
    if command == "":
        flag = True
    elif flag:
        parts.append(command)
    else:
        workflows.append(command)

class Workflow:
    def __init__(self, name, list_of_conditions):
        self.name = name
        self.list_of_conditions = list_of_conditions
        pass

    def evaluate(self, part : 'Part'):

        for (attribute, symbol, number), workflow_name in self.list_of_conditions[:-1]:
            if symbol == '<':
                if part.category[attribute] < number:
                    return workflow_name
            elif symbol == '>':
                if part.category[attribute] > number:
                    return workflow_name
        return self.list_of_conditions[-1]

class Part:
    def __init__(self, x, m, a, s):
        self.category = {
            'x': x,
            'm': m,
            'a': a,
            's': s 
        }
        pass

    def accepted(self):
        output = 'in'
        while output not in 'AR':
            #print(output)
            workflow = my_workflows[output]
            output = workflow.evaluate(self)

        if output == 'A':
            return True
        else:
            return False
        
    def sum_attributes(self):
        return sum(self.category.values())

my_workflows = {}
for workflow in workflows:
    name, second_part = workflow.split('{')
    second_part = second_part[:-1]
    list_of_conditions = second_part.split(',')
    list_of_conditions = [((condition[0], condition[1], int(condition.split(':')[0][2:])), condition.split(':')[1]) for condition in list_of_conditions[:-1]] + [list_of_conditions[-1]]
    my_workflows[name] = Workflow(name, list_of_conditions)

my_parts = []
for part in parts:
    part = part[1:-1].split(',')
    part = [int(attribute.split('=')[1]) for attribute in part]
    x, m, a, s = part
    my_parts.append(Part(x, m, a, s))

#pp.pprint(my_workflows)
#print(my_parts)
count = 0
for part in my_parts:
    if part.accepted():
        count += part.sum_attributes()
print(count)