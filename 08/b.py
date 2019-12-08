with open('input.txt') as f:
    x = f.readline()

w, h = 25, 6
N = int(len(x) / (w * h))
layers = [''] * N

img = ['0'] * w * h
done = [False] * w * h

minz = 100000
for i in range(N):
    layers[i] = str(x[i*w*h:(i+1)*w*h])
    for j in range(w*h):
        
        if not done[j] and layers[i][j] != '2':
            img[j] = layers[i][j]
            done[j] = True

msg = ''.join(img)
msg2 = msg.replace('0', ' ')

for i in range(h):
    print(msg2[i*w:(i+1)*w])

