def kod(k): #создаем функцию, увеличивающую элементы выбранной строки на 3
    for i in range(0, len(matriza)):
        matriza[n-1][i]=matriza[n-1][i]*3
    return matriza


matriza = [[2,5,7], #задаем матрицу
           [4,7,9],
           [1,2,0]]

n = int(input("Введите номер строки")) #получаем исходные данные
print(kod(n)) #выводим результат