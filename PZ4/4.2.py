# ���� ����� ����� N (> 1). ������� ���������� �� ����� ����� K, ��� ������� ����� 1 + 2 + ... + K
# ����� ������ ��� ����� N, � ���� ��� �����.
N = input("������� �������� N: ")   # ���� ����� N.
while type(N) != int:    # ��������� ����������.
    try:
        N = int(N)
    except ValueError:
        print("�������� ������ �� �������� �������������")
        N = input("������� ������ N: ")
amount = 0
K = 1
while amount < N:   # ���������� ���������.
    amount += K
    K += 1
print(K - 1)
print(amount)