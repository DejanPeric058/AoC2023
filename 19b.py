import pprint 
pp = pprint.PrettyPrinter(indent=4)
count = 0
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
        pass
    else:
        workflows.append(command)

class Workflow:
    def __init__(self, name, list_of_conditions):
        self.name = name
        self.list_of_conditions = list_of_conditions
        pass

    def evaluate(self, interval : 'Interval'):

        for (attribute, symbol, number), workflow_name in self.list_of_conditions[:-1]:
            if symbol == '<':
                if interval.end_part.category[attribute] < number:
                    if workflow_name == 'A':
                        return interval.combinations 
                    elif workflow_name == 'R':
                        return 0
                    else:
                        return my_workflows[workflow_name].evaluate(interval)
                elif interval.start_part.category[attribute] < number:
                    interval_low = Interval(start_part=interval.start_part, end_part=interval.end_part.change_value(attribute,number-1))
                    interval_high = Interval(start_part=interval.start_part.change_value(attribute, number), end_part=interval.end_part)
                    if workflow_name == 'A':
                        return interval_low.combinations + self.evaluate(interval_high)
                    elif workflow_name == 'R':
                        return self.evaluate(interval_high)
                    else:
                        return my_workflows[workflow_name].evaluate(interval_low) + self.evaluate(interval_high)
            elif symbol == '>':
                if interval.start_part.category[attribute] > number:
                    if workflow_name == 'A':
                        return interval.combinations 
                    elif workflow_name == 'R':
                        return 0
                    else:
                        return my_workflows[workflow_name].evaluate(interval)
                elif interval.end_part.category[attribute] > number:
                    interval_low = Interval(start_part=interval.start_part, end_part=interval.end_part.change_value(attribute,number))
                    interval_high = Interval(start_part=interval.start_part.change_value(attribute, number + 1), end_part=interval.end_part)
                    if workflow_name == 'A':
                        return interval_high.combinations + self.evaluate(interval_low)
                    elif workflow_name == 'R':
                        return self.evaluate(interval_low)
                    else:
                        return my_workflows[workflow_name].evaluate(interval_high) + self.evaluate(interval_low)
        last = self.list_of_conditions[-1]
        if last == 'A':
            return interval.combinations
        elif last == 'R':
            return 0
        else:
            return my_workflows[last].evaluate(interval)

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
        
    def change_value(self, attribute, value):
        dict1 = self.category.copy()
        dict1[attribute] = value
        return Part(dict1['x'], dict1['m'], dict1['a'], dict1['s'])
    
    
class Interval:
    def __init__(self, start_part : 'Part', end_part : 'Part'):
        self.start_part = start_part
        self.end_part = end_part
        self.combinations = self.calculate_combinations()

    def calculate_combinations(self):
        
        delta_x = self.end_part.category['x'] - self.start_part.category['x'] + 1
        delta_m = self.end_part.category['m'] - self.start_part.category['m'] + 1
        delta_a = self.end_part.category['a'] - self.start_part.category['a'] + 1
        delta_s = self.end_part.category['s'] - self.start_part.category['s'] + 1
        return delta_x * delta_m * delta_a * delta_s
        

my_workflows = {}
for workflow in workflows:
    name, second_part = workflow.split('{')
    second_part = second_part[:-1]
    list_of_conditions = second_part.split(',')
    list_of_conditions = [((condition[0], condition[1], int(condition.split(':')[0][2:])), condition.split(':')[1]) for condition in list_of_conditions[:-1]] + [list_of_conditions[-1]]
    my_workflows[name] = Workflow(name, list_of_conditions)


#pp.pprint(my_workflows)
#print(my_parts)

interval = Interval(Part(1,1,1,1), Part(4000, 4000, 4000, 4000))
count = my_workflows['in'].evaluate(interval)
print(count)