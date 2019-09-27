# Дан массив из 10 элементов. Отсортировать массив с 1 по 5 по возрастанию,
# а с 6 по 1- по убыванию
from bubble_sort import bubble_sort
numbers = [2, 5, 1, 7, 6, 7, 5, 4, 9, 0]
sortnumbers = bubble_sort(numbers[:5]) + bubble_sort(numbers[5:], True)
print(sortnumbers)
