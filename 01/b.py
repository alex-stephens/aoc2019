lines = [] 
with open('input.txt') as f:
    for x in f.readlines():
        lines.append(int(x))

ans = 0

for m in lines:
    fuel = int(m/3) - 2
    total = fuel

    while True:
        new =  int(fuel/3) - 2
        if new <= 0:
            break

        total += new 
        fuel = new

    ans += total

print(ans)