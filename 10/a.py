from math import gcd

asteroids = [] 
with open('input.txt') as f:
    for line in f.readlines():
        asteroids.append(line.rstrip())
print(*asteroids, sep='\n')


def GetVal(x, y, asteroids):
    return asteroids[y][x]


def CheckSight(p1, p2, asteroids):

    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2 and y1 == y2:
        return False

    if x1 == x2:
        diff = (0, (y2 - y1)//abs(y2 - y1))
    elif y1 == y2:
        diff = ((x2 - x1)//abs(x2 - x1), 0)
    else:
        dx, dy = abs(x1-x2), abs(y1-y2)
        g = gcd(dx, dy)
        diff = ((x2 - x1)//g, (y2 - y1)//g)

    p3 = (p1[0]+diff[0], p1[1]+diff[1])
    while p3 != p2:
        if GetVal(p3[0], p3[1], asteroids) == '#':
            return False
        p3 = (p3[0]+ diff[0], p3[1] + diff[1])

    return True

rows = len(asteroids)
cols = len(asteroids[0])

m = 0

for y1 in range(rows):
    for x1 in range(cols):

        if GetVal(x1, y1, asteroids) == '.': 
            continue 
        count = 0

        for y2 in range(rows):
            for x2 in range(cols):
                if GetVal(x2, y2, asteroids) == '.': continue 

                if x1 == x2 and y1 == y2: 
                    continue
                
                p1 = (x1, y1)
                p2 = (x2, y2)
                if CheckSight(p1, p2, asteroids):
                    count += 1

        m = max(m, count)

print(m)