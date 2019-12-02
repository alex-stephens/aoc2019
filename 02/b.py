lines = [] 
with open('input.txt') as f:
    for x in f.readlines():
        originput = list(map(int, x.split(',')))

target = 19690720

for noun in range(100):
    for verb in range(100):
        
        i = 0
        input = list(originput)
        input[1] = noun
        input[2] = verb

        while i < len(input) and input[i] != 99:

            if input[i] == 1:
                input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
            elif input[i] == 2:
                input[input[i+3]] = input[input[i+1]] * input[input[i+2]]

            i += 4

        if input[0] == target:
            print(100*noun + verb)
            break