import math
a = int(input())
bigr = int(input())
smallr = 0
if a <= bigr:
    b = math.sqrt(bigr**2 - a**2) if a < bigr else 0
    smallr = a if b > a else b
    print(smallr)
else:
    print('Невозможное условие')
