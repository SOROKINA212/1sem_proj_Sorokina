# Описать функцию AddRight(D, K), добавляющую к целому положительному числу K справа цифру D (D - входной параметр
# целого типа, лежащий в диапазоне 0-9, K - параметр целого типа являющийся одновременно входным и выходным). С помощью
# этой функции последовательно добавить к данному числу K справа данные цифры D1 и D2, выводя результат каждого
# добавления.
def AddRightDigit(D, K):  # определение функции AddRightDigit
    K = K * 10 + D  # умножаем K на 10 и прибавляем D, таким образом D станет последней цифрой
    return K  # возвращаем K

def inputK():  # функция для ввода числа K
    K = input('Введите целое число: ')
    while type(K) != int:
        try:
            K = int(K)
            return K  # возвращаем K, если ввод корректный
        except ValueError:
            print('Введите целое число!')
            K = input()

def inputD():   # функция для ввода цифры
    D = input('Введите цифру, кторую нужно добавить в конец: ')
    while type(D) != int:
        try:
            D = int(D)
            if D < 0 or D > 9:
                print('Вы ввели не цифру.')
                D = print()
            else:
                return D  # возвращаем D, если ввод корректный
        except ValueError:
            print('Введите цифру!')
            D = input()

K = inputK()

D1 = inputD()
K = AddRightDigit(D1, K)
print(K)

D2 = inputD()
K = AddRightDigit(D2, K)
print(K)