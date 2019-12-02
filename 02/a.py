lines = [] 
with open('input.txt') as f:
    for x in f.readlines():
        input = list(map(int, x.split(',')))

input[1] = 12
input[2] = 2
i = 0

while i < len(input) and input[i] != 99:

    if input[i] == 1:
        input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
    elif input[i] == 2:
        input[input[i+3]] = input[input[i+1]] * input[input[i+2]]

    i += 4

print(input[0])