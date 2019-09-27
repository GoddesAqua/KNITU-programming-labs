m = int(input())
n = int(input())
try:
    x = m + (m + n) / (m + (m / (m + n)))
    print(x)
except Exception:
    print('Деление на 0')
