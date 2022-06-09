# ������� ������� AddRight(D, K), ����������� � ������ �������������� ����� K ������ ����� D (D - ������� ��������
# ������ ����, ������� � ��������� 0-9, K - �������� ������ ���� ���������� ������������ ������� � ��������). � �������
# ���� ������� ��������������� �������� � ������� ����� K ������ ������ ����� D1 � D2, ������ ��������� �������
# ����������.
def AddRightDigit(D, K):  # ����������� ������� AddRightDigit
    K = K * 10 + D  # �������� K �� 10 � ���������� D, ����� ������� D ������ ��������� ������
    return K  # ���������� K

def inputK():  # ������� ��� ����� ����� K
    K = input('������� ����� �����: ')
    while type(K) != int:
        try:
            K = int(K)
            return K  # ���������� K, ���� ���� ����������
        except ValueError:
            print('������� ����� �����!')
            K = input()

def inputD():   # ������� ��� ����� �����
    D = input('������� �����, ������ ����� �������� � �����: ')
    while type(D) != int:
        try:
            D = int(D)
            if D < 0 or D > 9:
                print('�� ����� �� �����.')
                D = print()
            else:
                return D  # ���������� D, ���� ���� ����������
        except ValueError:
            print('������� �����!')
            D = input()

K = inputK()

D1 = inputD()
K = AddRightDigit(D1, K)
print(K)

D2 = inputD()
K = AddRightDigit(D2, K)
print(K)