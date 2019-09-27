def sign(x):
    s = 0 if x == 0 else 1 if x > 0 else -1
    return s


a = int(input())
b = int(input())
print(sign(a) + sign(b))
