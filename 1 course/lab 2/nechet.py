a = int(input())
b = int(input())
counter = 0
summa = 0
predel = range(a, b + 1)
for i in predel:
    if i % 2 == 1:
        counter += 1
        if counter <= 5:
            print(i)
        summa += i
print(summa)
