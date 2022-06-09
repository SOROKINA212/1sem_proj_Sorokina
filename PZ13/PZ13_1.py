from random import randint

prav = False

n = int(input("Введите N ")) #ввод данных
while prav != True:
    if n%2 != 0:
        print("Введите четное число")
        n = int(input("Введите N "))  # ввод данных
    else:
        prav = True

result = 0
polovina = []
counter = 0

lst = [randint(-100, 100) for i in range(n)] #создаем список со случайными значениями
print(lst)

for i in range(n):
    if i == n/2:
        break
    else:
        polovina.append(lst[i])
        counter += 1



func = lambda x,y: x*y <0 #задаём лямбда функцию


for j in range(counter): #находим произведение чисел меньше 0
    if func(polovina[j], polovina[j-1]) == True:
        result = polovina[j]*polovina[j-1]


print(result)
