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
dir, indir = 0, 0

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

for p in planets.keys():
    new = 1

    while planets[p].parent != 'COM':
        new += 1
        p = planets[p].parent

    indir += new
    dir += 1

print(indir)

