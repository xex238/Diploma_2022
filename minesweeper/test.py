import numpy as np
import collections
import copy
import time

def test1():
    s1 = [0, 0, 0, 0]
    s2 = np.zeros(4)

    s3 = np.resize(s1, (2, 2))
    print(s3)
    print(type(s3))

    if(collections.Counter(s1) == collections.Counter(s2)):
        print('Они равны!')

    print('type(s1) = ', type(s1))
    print('type(s2) = ', type(s2))
    print(type(list(s2)))

    s1.append(0)
def test2():
    test_num = 0
    res = [int(i) for i in list('{0:0b}'.format(test_num))]
    print("The converted binary list is : " + str(res))
def test3():
    if(False):
        i = 10
    print(i)
def test4():
    for i in range(5):
        for j in range(i, 5):
            print(i, j)
def test5():
    for i in range(5):
        for j in range(5):
            for k in range(3):
                print(i, j, k)
                if(k == 1):
                    break
                    break
def test6():
    s = set()
    a1 = list(np.zeros((3, 3)))
    a2 = list(np.zeros((3, 3)))
    a2[0][0] = 1

    for i in range(3):
        for j in range(3):
            result = (a1[i][j], a2[i][j])
            s.add(result)

    print(s)
def test7():
    s = ((0, 0), (0, 1), (1, 0), (1, 1))

    # ss = copy.copy(s)
    # print(s == ss)

    result = s.count((0, 2))
    # result = s.index((1, 2))
    print(result)
def test8():
    s = [[0, 0], [0, 1], [1, 0], [1, 1]]
    if([1, 2] in s):
        print('Значение в списке')
    else:
        print('Значение не в списке')
def test9():
    for i in range(3):
        print(i)
    for i in range(3, 10):
        print(i)
def test10():
    s = [[1, 1], 2, 3, 4]
    s_tuple = tuple(s)
    print(s_tuple)
def test11():
    s1 = [1, 2, 3, 4]
    s2 = [10, 11, 12, 13]
    s3 = 1
    s4 = 2
    result = [s1, s2, s3, s4]
    result_tuple = tuple(result)
    print(result_tuple)
def test12():
    l = 30
    w = 30
    a1 = np.zeros((l, w))
    a2 = np.zeros((l, w))
    a1[0][0] = 1
    a1[0][1] = 1
    a1[0][2] = 1
    a1[1][0] = 1
    a1[2][0] = 1

    a2[0][0] = 1
    a2[0][1] = 1
    a2[1][0] = 1

    counter = 1000000
    start_time = time.time()
    for i in range(counter):
        a3 = a1 - a2
    end_time = time.time()
    print('Время работы программы: ', end_time - start_time)

    a1 = np.zeros((3, 3))
    a2 = np.zeros((3, 3))
    a1[0][0] = 1
    a1[0][1] = 1
    a1[0][2] = 1
    a1[1][0] = 1
    a1[2][0] = 1

    a2[0][0] = 1
    a2[0][1] = 1
    a2[1][0] = 1

    start_time = time.time()
    for i in range(counter):
        a3 = a1 - a2
    end_time = time.time()
    print('Время работы программы: ', end_time - start_time)
def get_connect_cell(i1, i2, j1, j2, k1, k2):

def test13():
    i1 = 5
    j1 = 6
    k1 = np.zeros((3, 3))
    k1[0][2] = 1
    k1[1][2] = 1
    k1[2][2] = 1
    voc1 = 2

    i2 = 5
    j2 = 8
    k2 = np.zeros((3, 3))
    k2[0][0] = 1
    k2[1][0] = 1
    k2[2][0] = 1
    voc2 = 2

    delta_i = i1 - i2
    delta_j = j1 - j2
    if abs(delta_i) <= 2 and abs(delta_j) <= 2:
        voc = abs(voc1 - voc2)
        coords = []
        values1 = []
        for i in range(-delta_i, 3):
            for j in range(-delta_j, 3):
                coords.append([i1 - 1 + i, j1 - 1 + j])
                values1.append(k1[i][j])
        for i in range()


class class1:
    def __init__(self):
        self.i = 0
        self.j = 0

    def get_copy(self, my_class):
        self.i = copy.copy(my_class.i)
        self.j = copy.copy(my_class.j)

    def method1(self, i, j):
        my_class = class1()
        my_class.get_copy(self)

        my_class.i = self.i + i
        my_class.j = self.j + j

        return my_class.i, my_class.j

# test1()
# test2()
# test3()
# test4()
# test5()
# test6()
# test7()
# test8()
# test9()
# test10()
# test11()
test12()

'''
my_class = class1()
my_class.i = 2
my_class.j = 3
print(my_class.method1(5, 10))
'''