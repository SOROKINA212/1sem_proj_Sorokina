from statistics import mean


matriza = [[12,5,7], #задаем матрицу
           [4,6,0],
           [1,2,9]]

result = 0
mass = []
j =0
for i in range(0,len(matriza)): #записываем матрицу в одномерный массив
    if j == 3:
        break
    if matriza[i][j]%3 ==0:
        mass.append(matriza[i][j])
        print(matriza[i][j])
        j +=1

print(mass)
result = mean(mass) #находим среднее арифметическое элементов массива

print(result) #выводим результат