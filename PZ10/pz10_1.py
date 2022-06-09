with open("text.txt", 'r', encoding="UTF-8") as f: #открываем файл для чтения
    text = f.read() #записываем все его содержимое в переменную
    print(text)

with open("text2.txt", 'r', encoding="UTF-8") as g: #тоже самое, что и сверху
    new_text = g.read()
    print(new_text)


spisok1 = text.split() #создаем из строки список
spisok2 = new_text.split()
spisok3 = [] #пустой список для результата

spisok1 = list(map(int, spisok1)) #переводим из типа str в тип int
spisok2 = list(map(int, spisok2))
all = spisok1 + spisok2 #складываем два списка в один
schet = 0
otriz = 0
poloz = 0

for i in range(9): #находим одинаковые символы в списках
    if spisok1[i-1] == spisok2[i-1]:
        spisok3.append(spisok1[i])

for i in all: #считаем все элементы списка
    schet += 1



for i in range(18): #находим и считаем отрицательные элементы списка
    if all[i] < 0:
        otriz += 1

for i in range(18): #находим и считаем положительные элементы списка
    if all[i] > 0:
        poloz += 1


with open("new_text.txt", 'w+', encoding="UTF-8") as main: #создаем новый файл
    main.writelines(f'Элементы первого файла: {str(text)}\n') #записываем в него наши переменные с ответами
    main.writelines(f'Элементы второго файла: {str(new_text)}\n')
    main.writelines(f'Элементы первого файла во втором: {str(spisok3)}\n')
    main.writelines(f'Элементы второго файла в первом: {str(spisok3)}\n')
    main.writelines(f'Количество элементов: {str(schet)}\n')
    main.writelines(f'Количество отрицательных элементов: {str(otriz)}\n')
    main.writelines(f'Количество положительных элементов: {str(poloz)}\n')
