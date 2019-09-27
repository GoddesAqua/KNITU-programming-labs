# Написать функцию поиска максимума
def max(a, b):
    if a > b:
        return a
    else:
        return b


c, d = int(input()), int(input())
print(max(c, d))
