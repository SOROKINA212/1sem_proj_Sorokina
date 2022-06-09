# Дан список A размера N. Найти минимальный элемент из его элементов с четными номерами: A2, A4, A6 . . .
import random
N = input()   # Ввод размера списка A
A = []   # Создаём пустой список
A = [float(input()) for i in range(N)]

minA = float('inf')
for i in range(N):
    if i % 2 == 0 and A[i] < minA:
        minA = A[i]

print(minA)