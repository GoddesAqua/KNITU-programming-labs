# Дан список чисел.
# Если в нем есть два соседних элемента одного знака, выведите эти числа.
# Если соседних элементов одного знака нет — не выводите ничего.
# Если таких пар соседей несколько — выведите первую пару.


def sign(x):
    s = 0 if x == 0 else 1 if x > 0 else -1
    return s


numbers = [1, -2, 3, -5, -6, 7, 8]
for i in range(1, len(numbers)):
    if sign(numbers[i - 1]) == sign(numbers[i]):
        print(numbers[i - 1], numbers[i], sep=' ')
        break
