import re

with open('Dostoevsky.txt', 'r', encoding='UTF-8') as k: #открываем файл для чтения
    text = k.read() #записываем содержимое в переменную

data =0
result= re.findall(r'\d{4}', text) #задаем регулярное выржение для поиска всех чисел из 4 символов


for i in result: #ищем 1857
    if i == '1857':
        data  = i

print(text[text.find(data)+8 : text.find('В 1859')])

with open('new_txt.txt', 'w+', encoding='UTF-8') as b: #открываем файл для записи и записываем туда результат
    b.write(text[text.find(data)+8 : text.find('В 1859')])