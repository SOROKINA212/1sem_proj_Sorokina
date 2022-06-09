# Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N
N = input("Введите предел N: ")   #Ввод предела.
while type(N) !=int:    #Обработка исключений
    try:
        N = int(N)
    except ValueError:
        print("Введённый предел не является целочисленным. . . ")
        N = input("Введите предел N: ")
amount = 0
i = 1
while i <= N:   #Проведение рассчётов.
    amount += 1 / i
    i += 1

print(amount)