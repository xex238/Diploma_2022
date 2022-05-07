import numpy as np
import collections
import copy

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
test11()

'''
my_class = class1()
my_class.i = 2
my_class.j = 3
print(my_class.method1(5, 10))
'''