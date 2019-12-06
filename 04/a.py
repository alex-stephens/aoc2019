digits = 6

def isvalid(num):
    num = str(num)
    found = False

    for i in range(1, digits):
        if num[i] < num[i-1]:
            return False
        elif num[i] == num[i-1]:
            found = True
    return found

count = 0

for n in range(172930, 683082 + 1):
    count += 1 if isvalid(n) else 0

print(count)