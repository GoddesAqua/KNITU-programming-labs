import random
magic = 77
rnd = 0
while rnd != magic:
    rnd = random.randint(1, 100)
    if rnd > magic:
        print('Ваше число больше магического', rnd)
    elif rnd < magic:
        print('Ваше число меньше магического', rnd)
print('Вы угадали')
