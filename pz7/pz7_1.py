# Дан символ C и строка S. Удвоить каждое вхождение символа C в строку S.
def doubleSyymbol(s, c):  # объявляем функцию
    return s.replace(c, c * 2)  # в строке s заменяем каждое вхождение c на два символа c

s = input('Введите строку: ')
while True:   # проверка на ввод, с должен быть одним символом
    c = input('Введите символ: ')
    if len(c) == 1:
        break
    else:
        print('Введите один символ!')

print('Результат: ', doubleSyymbol(s, c))