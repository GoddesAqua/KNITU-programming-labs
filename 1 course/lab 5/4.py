# Написать программу, определяющую знак зодиака по введенной дате (число и месяц).
def январь(day):
    if day <= 19:
        return 'Козерог'
    else:
        return 'Водолей'


def февраль(day):
    if day <= 19:
        return 'Водолей'
    else:
        return 'Рыбы'


def март(day):
    if day <= 19:
        return 'Рыбы'
    else:
        return 'Овен'


def апрель(day):
    if day <= 19:
        return 'Овен'
    else:
        return 'Телец'


def май(day):
    if day <= 19:
        return 'Телец'
    else:
        return 'Близнецы'


def июнь(day):
    if day <= 19:
        return 'Близнецы'
    else:
        return 'Рак'


def июль(day):
    if day <= 19:
        return 'Рак'
    else:
        return 'Лев'


def август(day):
    if day <= 19:
        return 'Лев'
    else:
        return 'Дева'


def сентябрь(day):
    if day <= 19:
        return 'Дева'
    else:
        return 'Весы'


def октябрь(day):
    if day <= 19:
        return 'Весы'
    else:
        return 'Скорпион'


def ноябрь(day):
    if day <= 19:
        return 'Скорпион'
    else:
        return 'Стрелец'


def декабрь(day):
    if day <= 19:
        return 'Стрелец'
    else:
        return 'Козерог'


месяца = {
    1: январь,
    2: февраль,
    3: март,
    4: апрель,
    5: май,
    6: июнь,
    7: июль,
    8: август,
    9: сентябрь,
    10: октябрь,
    11: ноябрь,
    12: декабрь,
}
day = int(input())
month = int(input())
print(месяца.get(month)(day))
