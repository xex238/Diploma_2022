import numpy as np
import collections
import copy
import time
import matplotlib.pyplot as plt
# import matplotlib
import random
import xlrd

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
def test14():
    print(random.random() * 3 + 1)

# Считывание данных для отрисовки графика с накоплением для вычисления доли применения методов для каждого поля
def xlsx_open():
    # Open the Workbook
    workbook = xlrd.open_workbook("data2.xlsx")

    # Open the worksheet
    worksheet = workbook.sheet_by_index(0)

    method1 = []
    method2 = []
    method3 = []
    method4 = []

    # Iterate the rows and columns
    for i in range(1, 1076):
        method1.append(worksheet.cell_value(i, 1))
        method2.append(worksheet.cell_value(i, 2))
        method3.append(worksheet.cell_value(i, 3))
        method4.append(worksheet.cell_value(i, 4))
        for j in range(1, 5):
            # Print the cell values with tab space
            print(worksheet.cell_value(i, j), end='\t')
        print('')

    result = []
    result.append(np.array(method1))
    result.append(np.array(method2))
    result.append(np.array(method3))
    result.append(np.array(method4))

    result1 = np.array(result)
    # print(result1)

    return result1
# Считывание данных для отрисовки графика со временем поиска решения для каждого моля только с применением методов
def xlsx_open2():
    # Open the Workbook
    workbook = xlrd.open_workbook("data31.xlsx")

    # Open the worksheet
    worksheet = workbook.sheet_by_index(0)

    method1 = []

    # Iterate the rows and columns
    for i in range(0, 1075):
        method1.append(worksheet.cell_value(i, 0))

    return method1
# Считывание данных для отрисовки графика со временем поиска решения для каждого моля только с применением схем
def xlsx_open3():
    # Open the Workbook
    workbook = xlrd.open_workbook("data4.xlsx")

    # Open the worksheet
    worksheet = workbook.sheet_by_index(0)

    method1 = []

    # Iterate the rows and columns
    for i in range(0, 1075):
        method1.append(worksheet.cell_value(i, 0))

    return method1
# Считывание данных для отрисовки графика со временем поиска решения для каждого моля с применением методов и схем
def xlsx_open4():
    # Open the Workbook
    workbook = xlrd.open_workbook("data5.xlsx")

    # Open the worksheet
    worksheet = workbook.sheet_by_index(0)

    method1 = []

    # Iterate the rows and columns
    for i in range(0, 1075):
        method1.append(worksheet.cell_value(i, 0))

    return method1


# Отрисовка тестового графика
def draw_graphics():
    rng = np.arange(50)
    rnd = np.random.randint(0, 10, size=(3, rng.size))
    yrs = 1950 + rng

    print(rnd)

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
    ax.set_title('Combined debt growth over time')
    ax.legend(loc='upper left')
    ax.set_ylabel('Total debt')
    ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
    fig.tight_layout()

    plt.show()
# Отрисовка графика с накоплением для вычисления доли применения методов для каждого поля
def draw_graphics2(y):
    x = np.arange(1075)

    sum = np.zeros(len(y[0]))
    for i in range(len(y)):
        for j in range(len(y[i])):
            sum[j] += y[i][j]

    for i in range(len(sum)):
        sum[i] = 100 / sum[i]

    for i in range(len(y)):
        for j in range(len(y[i])):
            y[i][j] = y[i][j] * sum[j]

    fig, ax = plt.subplots(figsize=(12, 9))
    ax.stackplot(x, y, labels=['Процедура 1', 'Процедура 2', 'Процедура 4', 'Процедура 3'])
    ax.set_title('Процент применённых процедур', fontsize = 'xx-large')
    ax.legend(loc='upper right', fontsize = 'xx-large')
    ax.set_xlabel('Порядковый номер поля', fontsize = 'xx-large')
    ax.set_ylabel('%', fontsize = 'xx-large')
    ax.set_xlim(xmin=x[0], xmax=x[-1])
    fig.tight_layout()

    plt.show()
# Отрисовка графика со временем поиска решения для каждого моля только с применением методов
def draw_graphics3(y):
    x = np.arange(1075)

    fig, ax = plt.subplots(figsize=(12, 9))
    ax.stackplot(x, y)
    ax.set_title('Время поиска решения с применением процедур', fontsize = 'xx-large')
    ax.legend(loc='upper left')
    ax.set_xlabel('Порядковый номер поля', fontsize = 'xx-large')
    ax.set_ylabel('Секунды', fontsize = 'xx-large')
    ax.set_xlim(xmin=x[0], xmax=x[-1])
    fig.tight_layout()

    plt.show()
# Отрисовка графика со временем поиска решения для каждого моля только с применением схем
def draw_graphics4(y):
    x = np.arange(1075)

    fig, ax = plt.subplots(figsize=(12, 9))
    ax.stackplot(x, y)
    ax.set_title('Время поиска решения с применением схем', fontsize = 'xx-large')
    ax.legend(loc='upper left')
    ax.set_xlabel('Порядковый номер поля', fontsize = 'xx-large')
    ax.set_ylabel('Секунды', fontsize = 'xx-large')
    ax.set_xlim(xmin=x[0], xmax=x[-1])
    fig.tight_layout()

    plt.show()
# Отрисовка графика со временем поиска решения для каждого моля с применением методов и схем
def draw_graphics5(y):
    x = np.arange(1075)

    fig, ax = plt.subplots(figsize=(12, 9))
    ax.stackplot(x, y)
    ax.set_title('Время поиска решения с применением процедур и схем')
    ax.legend(loc='upper left')
    ax.set_ylabel('Секунды')
    ax.set_xlim(xmin=x[0], xmax=x[-1])
    fig.tight_layout()

    plt.show()


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
# test12()

'''
result = xlsx_open()
draw_graphics2(result)
'''

'''
result = xlsx_open2()
draw_graphics3(result)
'''


result = xlsx_open3()
draw_graphics4(result)


'''
result = xlsx_open4()
draw_graphics5(result)
'''

# draw_graphics()
#test14()

'''
my_class = class1()
my_class.i = 2
my_class.j = 3
print(my_class.method1(5, 10))
'''