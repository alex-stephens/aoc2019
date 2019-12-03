input = [] 
with open('input.txt') as f:
    for x in f.readlines():
        input.append(x.rstrip())

line1 = input[0].split(',')
line2 = input[1].split(',')

positions = {}
pos = [0,0]
steps = 0

for c in line1:
    num = int(c[1:])

    if c[0] == 'U':
        dir = (0, 1)
    if c[0] == 'D':
        dir = (0, -1)
    if c[0] == 'L':
        dir = (-1, 0)
    if c[0] == 'R':
        dir = (1, 0)

    for _ in range(num):
        pos[0] += dir[0]
        pos[1] += dir[1]
        steps += 1
        
        positions[tuple(pos)] = steps
        # print(pos)

pos = [0,0]
intersections = []
mindist = 100000000000000000000
steps = 0

for c in line2:

    num = int(c[1:])

    if c[0] == 'U':
        dir = (0, 1)
    if c[0] == 'D':
        dir = (0, -1)
    if c[0] == 'L':
        dir = (-1, 0)
    if c[0] == 'R':
        dir = (1, 0)

    for _ in range(num):
        pos[0] += dir[0]
        pos[1] += dir[1]
        steps += 1
        
        if tuple(pos) in positions:
            intersections.append(pos)
            mindist = min(mindist, steps + positions[tuple(pos)])

print(mindist)