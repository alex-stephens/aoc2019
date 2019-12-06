x = [] 
with open('input.txt') as f:
    for line in f.readlines():
        x.append(line.rstrip())
x = list(map(int, x[0].split(',')))

input = 5

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
    instr = None

    if code == 99:
        return None, -1, None

    output = None

    p1 = x[i+1] if modes[0] == 0 else i+1

    if code in (1,2,5,6,7,8):
        p2 = x[i+2] if modes[1] == 0 else i+2
    if code in (1,2,7,8):
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
    elif code == 5:
        if x[p1] != 0:
            instr = x[p2]
        length = 3
    elif code == 6:
        if x[p1] == 0:
            instr = x[p2]
        length = 3
    elif code == 7:
        if x[p1] < x[p2]:
            x[p3] = 1
        else:
            x[p3] = 0
        length = 4
    elif code == 8:
        if x[p1] == x[p2]:
            x[p3] = 1
        else:
            x[p3] = 0
        length = 4
    else:
        print("Bad opcode")

    return output, length, instr
    
result = None

while True:
    val = x[i]
    code, modes = Parse(val)

    output, length, instr = GetOutput(code, modes, i)

    # received 99 
    if length == -1:
        break

    if output is not None:
        result = output

    if instr is None:
        i +=  length
    else:
        i = instr

print(result)