# ��� ������ A ������� N. ����� ����������� ������� �� ��� ��������� � ������� ��������: A2, A4, A6 . . .
import random
N = input()   # ���� ������� ������ A
A = []   # ������ ������ ������
A = [float(input()) for i in range(N)]

minA = float('inf')
for i in range(N):
    if i % 2 == 0 and A[i] < minA:
        minA = A[i]

print(minA)