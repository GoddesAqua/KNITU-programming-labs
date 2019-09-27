# Имеется массив из 5 элементов.
# Вывести среднее арифметическое отрицательных элементов.
numbers = [1, -2, -5, -3, -8, 6, 7, 8]
summ, count = 0, 0
for i in numbers:
    if i < 0:
        summ += i
        count += 1
print(summ / count)
