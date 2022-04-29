import numpy as np
import copy
import collections
import math

class minesweeper:
    def __init__(self):
        self.l = 5 # Количество строк
        self.w = 5 # Количество столбцов
        # Значения клеток
        self.values = [[0, 0, 1, -1, 0], [0, 0, 1, 2, -1], [1, 1, 0, 1, 1], [-1, 1, 0, 0, 0], [0, 1, 0, 0, 0]]
        # Статус клеток
        self.status = [[True, True, True, False, False], [True, True, True, True, False], [True, True, True, True, True], [False, True, True, True, True], [False, True, True, True, True]]
        self.values_known = np.resize(self.values, self.l * self.w) # Известные значения
        self.values_mas = np.resize(self.values, self.l * self.w) # Список значений
        self.status_mas = np.resize(self.status, self.l * self.w) # Список статусов

        self.near_values = []
        self.near_values_known = []
        self.near_values_unknown = []

        self.coordinates = [] # Номера уравнений в системе уравнений

        self.x = []
        self.y = []

    def matrix_x(self):
        x = []
        for i in range(len(self.x)):
            x.append(np.resize(self.x[i], (self.l, self.w)))

        return x

    def matrix_y(self):
        return np.resize(self.y, (self.l, self.w))

    # Перевести координаты в число
    def coords_to_number(self, coordinates):
        return coordinates[0] * self.l + coordinates[1]

    # Перевести число в координаты
    def number_to_coords(self, number):
        result = []
        result.append(math.floor(number / self.w))
        result.append(number % self.w)

        return result

    # Перевести список координат в список чисел
    def coords_list_to_numbers_list(self, coords_list):
        result = []
        for i in range(len(coords_list)):
            result.append(self.coords_to_number(coords_list[i]))

        return result

    # Перевести список чисел в список координат
    def numbers_list_to_coords_list(self, numbers_list):
        result = []
        for i in range(len(numbers_list)):
            result.append(self.number_to_coords(numbers_list[i]))

    # Получить список координат соседних клеток по координате
    def get_near_values_on_coords(self, i, j):
        result = []
        if ((i == 0) and (j == 0)):
            result.append((i, j + 1))
            result.append((i + 1, j))
            result.append((i + 1, j + 1))
        elif ((i == 0) and ((j > 0) and (j < self.w - 1))):
            result.append((i, j - 1))
            result.append((i + 1, j - 1))
            result.append((i + 1, j))
            result.append((i + 1, j + 1))
            result.append((i, j + 1))
        elif ((i == 0) and (j == self.w - 1)):
            result.append((i, j - 1))
            result.append((i + 1, j - 1))
            result.append((i + 1, j))
        elif (((i > 0) and (i < self.l - 1)) and (j == self.w - 1)):
            result.append((i - 1, j))
            result.append((i - 1, j - 1))
            result.append((i, j - 1))
            result.append((i + 1, j - 1))
            result.append((i + 1, j))
        elif ((i == self.l - 1) and (j == self.w - 1)):
            result.append((i - 1, j))
            result.append((i - 1, j - 1))
            result.append((i, j - 1))
        elif ((i == self.l - 1) and ((j > 0) and (j < self.w - 1))):
            result.append((i, j - 1))
            result.append((i - 1, j - 1))
            result.append((i - 1, j))
            result.append((i - 1, j + 1))
            result.append((i, j + 1))
        elif ((i == self.l - 1) and (j == 0)):
            result.append((i - 1, j))
            result.append((i - 1, j + 1))
            result.append((i, j + 1))
        elif (((i > 0) and (i < self.l - 1)) and (j == 0)):
            result.append((i - 1, j))
            result.append((i - 1, j + 1))
            result.append((i, j + 1))
            result.append((i + 1, j + 1))
            result.append((i + 1, j))
        elif (((i > 0) and (i < self.l - 1)) and ((j > 0) and (j < self.w - 1))):
            result.append((i - 1, j - 1))
            result.append((i - 1, j))
            result.append((i - 1, j + 1))
            result.append((i, j - 1))
            result.append((i, j + 1))
            result.append((i + 1, j - 1))
            result.append((i + 1, j))
            result.append((i + 1, j + 1))

        return result

    # Нумерация клеток поля
    def get_coords(self):
        for i in range(self.l):
            for j in range(self.w):
                self.coordinates.append(self.coords_to_number((i, j)))

    # Получение известных значений поля
    def get_values_known(self):
        for i in range(len(self.status_mas)):
            if(not self.status_mas[i]):
                self.values_known[i] = -10

    # Получение списков с соседними клетками
    def get_near_values(self):
        for i in range(self.l):
            for j in range(self.w):
                helper = np.zeros((self.l, self.w))
                helper_know = np.zeros((self.l, self.w))
                helper_unknown = np.zeros((self.l, self.w))

                result = self.get_near_values_on_coords(i, j)
                for k in range(len(result)):
                    helper[result[k][0]][result[k][1]] = 1
                    if(self.status[result[k][0]][result[k][1]]):
                        helper_know[result[k][0]][result[k][1]] = 1
                    else:
                        helper_unknown[result[k][0]][result[k][1]] = 1

                helper1 = np.resize(helper, self.l * self.w)
                helper_know1 = np.resize(helper_know, self.l * self.w)
                helper_unknown1 = np.resize(helper_unknown, self.l * self.w)
                self.near_values.append(helper1)
                self.near_values_known.append(helper_know1)
                self.near_values_unknown.append(helper_unknown1)

    # Получить список соседних закрытых клеток
    def get_near_close(self, number):
        c = self.number_to_coords(number)
        result = self.get_near_values_on_coords(c[0], c[1])

        result1 = []
        for i in range(len(result)):
            if(self.status[result[i][0]][result[i][1]] == False):
                result1.append(result[i])
        result2 = self.coords_list_to_numbers_list(result1)

        list_x = np.zeros(self.l * self.w)
        for i in range(len(result2)):
            list_x[result2[i]] = 1

        return list_x

    # Уменьшение системы уравнений
    def cutting(self):
        self.x = copy.copy(self.near_values_unknown)
        self.y = copy.copy(self.values_mas)

        # Удаляем строки, где значение y[i] неизвестно (клетка закрыта)
        rows = []
        for i in range(len(self.status_mas)):
            if(not self.status_mas[i]):
                rows.append(i)

        x1 = np.delete(self.x, rows, axis=0)
        y1 = np.delete(self.y, rows)
        coords1 = np.delete(self.coordinates, rows)

        # Удаляем равенства из системы
        helper_mas = np.zeros(self.l * self.w)
        zeros_counter = collections.Counter(helper_mas)
        rows = []
        for i in range(len(y1)):
            if(collections.Counter(x1[i]) == zeros_counter):
                rows.append(i)

        if(len(rows) != 0):
            x2 = np.delete(x1, rows, axis=0)
            y2 = np.delete(y1, rows)
            coords2 = np.delete(coords1, rows)

        coordinates = copy.copy(coords2)

        '''
        print('x2 = ')
        print(x2)
        print('y2 = ')
        print(y2)
        print()
        '''

        self.x = copy.copy(x2)
        self.y = copy.copy(y2)

    # Удаление из системы уравнений уравнения с заданным номером
    def delete_equals(self, n):
        mas_n = [n]
        x1 = np.delete(self.x, mas_n, axis=0)
        y1 = np.delete(self.y, mas_n)
        coords1 = np.delete(self.coordinates, mas_n)

        coordinates = copy.copy(coords1)

        self.x = copy.copy(x1)
        self.y = copy.copy(y1)

    # Реализация метода 1
    def method1(self):
        changes = False
        for i in range(len(self.x)):
            counter = 0
            helper_mas = []
            for j in range(len(self.x[i])):
                counter = counter + self.x[i][j]
                if(self.x[i][j] == 1):
                    helper_mas.append(j)

            if(counter == self.y[i]):
                changes = True
                for k in range(len(helper_mas)):
                    self.values_known[helper_mas[k]] = -1
                    for i1 in range(len(self.x)):
                        if(self.x[i1][k] == 1):
                            self.x[i1][k] = 0
                            self.y[i1] == self.y[i1] - 1
            elif(self.y[i] == 0):
                changes = True
                for k in range(len(helper_mas)):
                    self.values_known[helper_mas[k]] = self.values_mas[helper_mas[k]]
                    self.y.append(self.values_known[helper_mas[k]])
                    self.x.append(self.get_near_close(helper_mas[i]))
                    for i1 in range(len(self.x)):
                        self.x[i1][k] = 0
        return changes

if __name__ == "__main__":
    my_minesweeper = minesweeper()

    my_minesweeper.get_coords()
    my_minesweeper.get_near_values()
    my_minesweeper.cutting()

    # print(my_minesweeper.x)
    # print(my_minesweeper.y)
    print(my_minesweeper.matrix_x())
    print(my_minesweeper.y)
    exit(0)

    counter = 0
    while(True):
        if(not my_minesweeper.method1()):
            break
        counter = counter + 1
        print(counter)