def fibonachi(x):
    if x < 0:
        res = 'Error'
    elif x == 0:
        res = 0
    elif x == 1:
        res = 1
    else:
        res = fibonachi(x - 1) + fibonachi(x - 2)
    return res


N = int(input())
print(fibonachi(N))
