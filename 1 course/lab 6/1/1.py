# Дана строка, состоящая из слов, разделенных пробелами.
# Определите, сколько в ней слов. Используйте для решения задачи метод count.
# Сохраняйте файлы input и output в кодировке UTF-8
ввод = open('input.txt', 'r', encoding='utf-8')
s = ввод.read()
ввод.close()
вывод = open('output.txt', 'w', encoding='utf-8')
вывод.write(str(s.count(' ') + 1))
вывод.close()
