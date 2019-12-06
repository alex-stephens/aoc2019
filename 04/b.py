digits = 6

def isvalid(num):
    string = str(num)

    found = False
    currep = 1

    for i in range(1, digits):
        if string[i] < string[i-1]:
            return False

        if string[i] == string[i-1]:
            currep += 1
        else:
            if currep == 2:
                found = True
            currep = 1
    return found or currep == 2

count = 0

for n in range(172930, 683082 + 1):
    if isvalid(n):
        count += 1

print(count)