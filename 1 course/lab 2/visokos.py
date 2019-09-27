god = int(input())
visokos = ('YES'
           if (god % 4 == 0 and god % 100 != 0) or (god % 400 == 0)
           else 'NO')
print(visokos)
