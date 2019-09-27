minute = int(input('Число минут: '))
clockh = '0' + str((minute // 60) % 24)
clockm = '0' + str(minute % 60)
print(clockh[-2:], ':', clockm[-2:])
