from math import ceil

class Unit(object):
    def __init__(self, data):
        data = data.split(' ')
        print(data)
        self.name = data[1]
        self.qty = int(data[0])

    def __str__(self):
        return self.name + ' ' + str(self.qty)

    def Multiply(self, val):
        self.qty *= val
        return self

class Reaction(object):

    def __init__(self, inputs, output):
        self.inputs = inputs
        self.output = output

    def Required(self, req):
        '''
        Returns inputs required to make some quantity
        of the output.
        '''

        fac = ceil(req / self.output.qty)
        return [u.Multiply(fac) for u in self.inputs]

    def IsRequired(self, ingredient):
        for u in self.inputs:
            if u.name == ingredient:
                return True
        return False

reactions = {}

with open('input.txt') as f:
    for line in f.readlines():
        print(line)
        inputs = [Unit(s.strip()) for s in line.split('=>')[0].split(',')]
        output = Unit(line.split('=>')[1].strip())
        reactions[output.name] = Reaction(inputs, output)


def RequiredOre(fuel):

    req = {'FUEL' : Unit(str(fuel) + ' FUEL')}
    ore = 0

    while len(req) > 0:
        
        # find the required ingredient that is not required
        # by any other reactions 
        for r in req:
            
            required = False
            for q in reactions:
                if reactions[q].IsRequired(req[r].name):
                    required = True
                    break

            if not required:
                u = req[r]
                req.pop(r)
                break

        # inputs to make the new ingredient
        new = reactions[u.name].Required(u.qty)
        reactions.pop(r) # this recipe won't be used again

        for n in new: 
            
            if n.name == 'ORE':
                ore += n.qty
                continue

            if n.name in req:
                req[n.name].qty += n.qty
            else:
                req[n.name] = n

    return ore


print('Required ore:', RequiredOre(1))