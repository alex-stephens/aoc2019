lines = [] 
with open('input.txt') as f:
    for x in f.readlines():
        lines.append(int(x))

ans = 0
for m in lines:
    ans += int(m/3) - 2

print(ans)