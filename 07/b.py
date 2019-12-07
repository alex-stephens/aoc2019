from itertools import permutations

with open('input.txt') as f:
    orig = list(map(int, f.readline().split(',')))


def Parse(val):
    val = str(val)
    code = int(val[-2:])

    modes = [0]*3
    modestr = val[:-2][::-1]
    for i, c in enumerate(modestr):
        modes[i] = int(c)

    return code, modes


class Computer(object):

    def __init__(self, program):
        self.program = list(program)
        self.orig = list(program)
        self.i = 0
        self.j = 0
        self.input = []
        self.output = None
        self.terminate = False

    def AddInput(self, val):
        self.input.append(val)

    def Restart(self):
        self.program = list(self.orig)
        self.i = 0
        self.j = 0
        self.input = []
        self.output = None
        self.terminate = False
        self.pause = False

    def RunProgram(self):
        self.pause = False
        
        while True:
            self.RunIteration()
            if self.pause or self.terminate:
                return

    def RunIteration(self):
        instrlength = {1:4,2:4,3:2,4:2,5:3,6:3,7:4,8:4,99:-1}

        i = self.i
        code, modes = Parse(self.program[i])

        if code == 99:
            self.terminate = True
            return

        x = list(self.program)
        instr = None

        p1 = x[i+1] if modes[0] == 0 else i+1

        if code in (1,2,5,6,7,8):
            p2 = x[i+2] if modes[1] == 0 else i+2
        if code in (1,2,7,8):
            p3 = x[i+3] if modes[2] == 0 else i+3

        if code == 1:
            x[p3] = x[p1] + x[p2]
        elif code == 2:
            x[p3] = x[p1] * x[p2] 
        elif code == 3:
            x[p1] = self.input[self.j]
            self.j += 1
        elif code == 4:
            self.output = x[p1]
            self.pause = True
        elif code == 5:
            if x[p1] != 0:
                instr = x[p2]
        elif code == 6:
            if x[p1] == 0:
                instr = x[p2]
        elif code == 7:
            if x[p1] < x[p2]:
                x[p3] = 1
            else:
                x[p3] = 0
        elif code == 8:
            if x[p1] == x[p2]:
                x[p3] = 1
            else:
                x[p3] = 0
        else:
            print("Bad opcode")

        length = instrlength[code]
        if instr is None:
            self.i +=  length
        else:
            self.i = instr

        self.program = list(x)


ans = -1000000

for p in permutations(range(5,10)):
 
    c = [Computer(orig) for _ in range(5)]
    inval = 0

    for i in range(5):
        c[i].AddInput(p[i])

    while not c[4].terminate:
        for i in range(5):
            c[i].AddInput(inval)
            c[i].RunProgram()
            inval = c[i].output 

    ans = max(ans, c[4].output)

print(ans)