# Имеется двумерный массив 4х4. заполнить его с клавиатуры.
# Отсортировать глав диагональ по возрастанию, побочную по убыванию
from bubble_sort import bubble_sort
array = [[int(input()) for i in range(4)] for i in range(4)]
gdg = bubble_sort([array[i][i] for i in range(4)])
pdg = bubble_sort([array[3 - i][i] for i in range(4)], True)
for i in range(4):
    array[i][i] = gdg[i]
    array[i][3 - i] = pdg[i]
for row in array:
    for elem in row:
        print(elem, end=' ')
    print()
