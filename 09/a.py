from itertools import permutations

with open('input.txt') as f:
    orig = list(map(int, f.readline().split(',')))

for _ in range(100000):
    orig.append(0)

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
        self.relbase = 0

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
        self.relbase = 0

    def RunProgram(self):
        self.pause = False
        
        while True:
            self.RunIteration()
            if self.pause or self.terminate:
                return

    def RunIteration(self):
        instrlength = {1:4,2:4,3:2,4:2,5:3,6:3,7:4,8:4,9:2,99:-1}

        i = self.i
        code, modes = Parse(self.program[i])

        if code == 99:
            self.terminate = True
            return

        x = list(self.program)
        instr = None

        if modes[0] == 0:
            p1 = x[i+1]
        elif modes[0] == 1:
            p1 = i+1
        else:
            p1 = x[i+1] + self.relbase

        if code in (1,2,5,6,7,8):
            if modes[1] == 0:
                p2 = x[i+2]
            elif modes[1] == 1:
                p2 = i+2
            else:
                p2 = x[i+2] + self.relbase

        if code in (1,2,7,8):
            if modes[2] == 0:
                p3 = x[i+3]
            elif modes[2] == 1:
                p3 = i+3
            else:
                p3 = x[i+3] + self.relbase

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
        elif code == 9:
            self.relbase = self.relbase + x[p1]
        else:
            print("Bad opcode")

        length = instrlength[code]
        if instr is None:
            self.i +=  length
        else:
            self.i = instr

        self.program = list(x)


ans = -1000000

c = Computer(orig)
c.AddInput(1)
c.RunProgram()
while not c.terminate:
    print(c.output)
    c.RunProgram()
