# Ввести массив 3х3.
# посчитать сумму главной диагонали.
# Отсортировать главную диагональ по возрастанию
from bubble_sort import bubble_sort
array = [[int(input()) for i in range(4)] for i in range(4)]
gdg = bubble_sort([array[i][i] for i in range(4)])
summ = sum(gdg)
for i in range(4):
    array[i][i] = gdg[i]
for row in array:
    for elem in row:
        print(elem, end='\t')
    print()
print('Сумма: ', summ)
