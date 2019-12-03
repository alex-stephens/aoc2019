input = [] 
with open('input.txt') as f:
    for x in f.readlines():
        input.append(x.rstrip())

line1 = input[0].split(',')
line2 = input[1].split(',')

positions = set()
pos = [0,0]

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
        
        positions.add((tuple(pos)))

pos = [0,0]
intersections = []
mindist = 100000000000000000000

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
        
        if tuple(pos) in positions:
            intersections.append(pos)
            mindist = min(mindist, abs(pos[0]) + abs(pos[1]))

print(mindist)