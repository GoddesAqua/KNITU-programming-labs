N = int(input('Введите число N: '))
for i in range(1, N):
    if i**2 > N:
        break
    print(i**2)
