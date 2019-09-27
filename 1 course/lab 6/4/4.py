# Дана строка. Замените в этой строке все появления буквы h на букву H,
# кроме первого и последнего вхождения.
# Сохраняйте файлы input и output в кодировке UTF-8
ввод = open('input.txt', 'r', encoding='utf-8')
s = ввод.read()
ввод.close()
s = s[:s.find('h') + 1] + s[s.find('h') + 1:s.rfind('h')
                            ].replace('h', 'H') + s[s.rfind('h'):]
вывод = open('output.txt', 'w', encoding='utf-8')
вывод.write(s)
вывод.close
