# ���� ����� ����� N (>0). ����� ����� 1 + 1/2 + 1/3 + ... + 1/N
N = input("������� ������ N: ")   #���� �������.
while type(N) !=int:    #��������� ����������
    try:
        N = int(N)
    except ValueError:
        print("�������� ������ �� �������� �������������. . . ")
        N = input("������� ������ N: ")
amount = 0
i = 1
while i <= N:   #���������� ���������.
    amount += 1 / i
    i += 1

print(amount)