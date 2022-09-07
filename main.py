from ast import Mult
from operator import truediv
import numpy as np


def Plus(a, b):
    print(a, '+', b, '=', a+b)


def Minus(a, b):
    print(a, '-', b, '=', a-b)


def Multiply(a, b):
    print(a, '*', b, '=', a*b)


def Division(a, b):
    print(a, '/', b, '=', a/b)


def MatrixPlus(A, B, C, m, n):
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return (C)


def MatrixMultiply(A, B):
    A = np.array(A)
    B = np.array(B)
    return (A.dot(B))


def Back(checker):
    checker = False
    return (checker)


def Floats():
    print("Введите нужное вам действие \n")
    checker = True

    while (checker == True):
        case = input()

        match case:
            case '+':
                print('Введите числа в формате a + b построчно')
                try:
                    a = int(input())
                    b = int(input())
                    Plus(a, b)
                except:
                    print('Введены некорректные данные')
            case '-':
                print('Введите числа в формате a - b построчно')
                try:
                    a = int(input())
                    b = int(input())
                    Minus(a, b)
                except:
                    print('Введены некорректные данные')
            case '*':
                print('Введите числа в формате a * b построчно')
                try:
                    a = int(input())
                    b = int(input())
                    Multiply(a, b)
                except:
                    print('Введены некорректные данные')
            case '/':
                print('Введите числа в формате a / b построчно')
                try:
                    a = int(input())
                    b = int(input())
                    Division(a, b)
                except:
                    print('Введены некорректные данные')
            case _:
                print('Введите корректное действие')


def Matrix():
    print("Введите нужное вам действие \n")
    checker = True

    while (checker == True):
        case = input()

        match case:
            case '+':
                print('Введите размерность матрицы m x n построчно')
                m = int(input())
                n = int(input())
                A = [[0] * m] * n
                B = [[0] * m] * n
                C = [[0] * m] * n
                print('Построчно введите элементы матрицы A слева-направо сверху вниз')
                for i in range(m):
                    for j in range(n):
                        A[i][j] = int(input())
                print(
                    '\n Построчно введите элементы матрицы A слева-направо сверху вниз')
                for i in range(m):
                    for j in range(n):
                        A[i][j] = int(input())
                print(MatrixPlus(A, B, C, m, n))
            case '*':
                print('Введите размерность матрицы A (m x n) построчно')
                mA = int(input())
                nA = int(input())
                A = [[0] * mA] * nA

                print('\nВведите размерность матрицы B (m x n) построчно')
                mB = int(input())
                nB = int(input())
                B = [[0] * mB] * nB

                if mA != nB:
                    print('Невозможно перемножить данные матрицы')
                    Matrix()
                else:
                    print(
                        'Построчно введите элементы матрицы A слева-направо сверху вниз')
                    for i in range(mA):
                        for j in range(nA):
                            A[i][j] = int(input())
                    print(
                        '\n Построчно введите элементы матрицы B слева-направо сверху вниз')
                    for i in range(mB):
                        for j in range(nB):
                            B[i][j] = int(input())
                    C = MatrixMultiply(A, B)
                    print(C)
            case _:
                print('Введите корректное действие')

def main():
    print('Выберите режим: f - вещественные m - матрицы')
    mode = input()
    while mode != 'q':
        match mode:
            case 'f':
                Floats()
            case 'm':
                Matrix()
            case 'q':
                mode = 'q'
            case _:
                print("Неверный код режима")
                mode = input()


if __name__ == '__main__':
    main()