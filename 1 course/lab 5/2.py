# Составить программу, которая в зависимости от порядкового номера месяца,
# выводит на экран время года.
month = int(input())
if (month in range(1, 3)) or month == 12:
    print('Зима')
elif month in range(3, 6):
    print('Весна')
elif month in range(6, 9):
    print('Лето')
elif month in range(10, 12):
    print('Осень')
