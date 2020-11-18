import numpy as np
import itertools


def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix


def moves(count):
    """ The function creates a list of the permutations"""
    numline = []
    for i in range(0, count):
        numline.append(i)
    return list(itertools.permutations(numline, count))

def multiplication(num):
    """ The function adds matrix elements to the new list named 'm'
    according to permutation, multiplied by returned element from function 'index()' """
    def index(ind):
        """The function return minus one to the extent of the number
        of inversions in the permutation"""
        N = 0
        for i in range(0, len(ind)-1):
            for k in range(i+1, len(ind)):
                if ind[i] > ind[k]:
                    N += 1
        return (-1) ** N
    m = []
    for i in range(0, len(per)):
        m.append(1)
        for k in range(0, len(per[i])):
            m[i] = m[i] * a[k][per[i][k]]
        m[i] = m[i] * index((per[i]))

    return m


def sum(mult):
    """ The function sums the element of the tuple
    returned by function 'multiplication()' """
    s = 0
    for i in range(0, len(mult)):
        s += mult[i]
    return s


def getNumber(support_text):
    """ The function checks the number for compliance with the task conditions"""
    while True:
        getTempNumber = input(support_text)
        try:
            getTempNumber = int(getTempNumber)
        except ValueError:
            print(f'"{getTempNumber}" Не є цілим числом')
        else:
            if getTempNumber < 1:
                print(f'"{getTempNumber}" Матриця повинна мати хоча б один елемент.'
                      f' Введіть заново')
            else:
                break

    return getTempNumber


n = getNumber('Розмірність: ')
a = random_matrix(n)
print('Матриця: \n', a)
per = moves(n)

print('Результат: ', sum(multiplication(per)))
print('Додаткова перевірка: ', round(np.linalg.det(a)))
