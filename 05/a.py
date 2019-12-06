x = [] 
with open('input.txt') as f:
    for line in f.readlines():
        x.append(line.rstrip())
x = list(map(int, x[0].split(',')))

input = 1

i = 0

def Parse(val):
    val = str(val)
    code = int(val[-2:])

    modes = [0]*3
    modestr = val[:-2][::-1]
    for i, c in enumerate(modestr):
        modes[i] = int(c)

    return code, modes

def GetOutput(code, modes, i):

    if code == 99:
        return None, -1

    output = None

    p1 = x[i+1] if modes[0] == 0 else i+1

    if code == 1 or code == 2:
        p2 = x[i+2] if modes[1] == 0 else i+2
        p3 = x[i+3] if modes[2] == 0 else i+3

    if code == 1:
        x[p3] = x[p1] + x[p2]
        length = 4
    elif code == 2:
        x[p3] = x[p1] * x[p2] 
        length = 4
    elif code == 3:
        x[p1] = input
        length = 2
    elif code == 4:
        output = x[p1]
        length = 2

    return output, length
    
result = None

while True:
    val = x[i]
    code, modes = Parse(val)

    output, length = GetOutput(code, modes, i)

    # received 99 
    if length == -1:
        break

    if output is not None:
        result = output
    i +=  length

print(result)