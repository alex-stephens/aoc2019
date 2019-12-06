x = [] 
with open('input.txt') as f:
    for line in f.readlines():
        x.append(line.rstrip())

class Planet(object):

    def __init__(self, id):
        self.id = id
        self.parent = None
        self.children = 0

planets = dict()

def AddPlanet(p):
    if p in planets or p == 'COM':
        return
    else:
        planets[p] = Planet(p)
    
for c in x:
    a, b = c.split(')')
    AddPlanet(a)
    AddPlanet(b)
    planets[b].parent = a

t1 = planets['YOU'].parent
t2 = planets['SAN'].parent

ancestors = {t1:0}
num = 1
while t1 != 'COM':
    t1 = planets[t1].parent
    ancestors[t1] = num
    num = num + 1

num = 0
while t2 not in ancestors.keys():
    num += 1
    t2 = planets[t2].parent

print(num + ancestors[t2])