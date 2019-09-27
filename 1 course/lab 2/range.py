a = int(input())
b = int(input())
predel = range(a, b + 1) if a < b else range(a, b - 1, -1)
for i in predel:
    print(i)
