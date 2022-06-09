def uppercase(stroka):  #задаём функцию для перевода букв в верхний регистр
    for i in stroka:
        i = i.upper()

        yield i

n = input("Введите строку")   #получаем исходные данные
fraza = list(n.split())  #переводим строку в список
rezult = []

generator = uppercase(fraza)  #создаём генератор

for j in generator:   #записываем результат
    rezult.append(j)

print(rezult)