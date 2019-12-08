with open('input.txt') as f:
    x = f.readline()

w, h = 25, 6
N = int(len(x) / (w * h))
layers = [''] * N

minz = 100000
for i in range(N):
    layers[i] = str(x[N*i:N*i+w*h])
    
    zeros = layers[i].count('0')
    if zeros < minz:
        L = i
        minz = zeros

print(layers[L].count('1') * layers[L].count('2'))

