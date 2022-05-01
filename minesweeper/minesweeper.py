import numpy as np
import copy
import collections
import math

class Minesweeper:
    def __init__(self):
        self.l = 0 # Количество строк
        self.w = 0 # Количество столбцов
        self.count_of_mines = -1 # Количество мин на поле

        self.true_values = [] # Значения клеток в виде матрицы
        self.true_values_mas = [] # Список значений клеток

        self.status = [] # Статус клеток в виде матрицы
        self.status_mas = [] # Список статусов клеток

        self.values_known = [] # Список известных значений клеток

        self.x = [] # Значения x системы уравнений
        self.y = [] # Значения y системы уравнений

    ##########
    ### Работа с исходными данными
    # Загрузка тестовых данных
    def load_data(self):
        self.l = 5 # Количество строк
        self.w = 5 # Количество столбцов
        self.count_of_mines = 3 # Количество мин на поле
        # Значения клеток в виде матрицы
        self.true_values = [[0, 0, 1, -1, 2], [0, 0, 1, 2, -1], [1, 1, 0, 1, 1], [-1, 1, 0, 0, 0], [1, 1, 0, 0, 0]]
        self.true_values_mas = np.resize(self.true_values, self.l * self.w) # Список значений клеток
        # Статус клеток в виде матрицы
        self.status = [[True, True, True, False, False], [True, True, True, True, False], [True, True, True, True, True], [False, True, True, True, True], [False, True, True, True, True]]
        self.status_mas = np.resize(self.status, self.l * self.w) # Список статусов клеток

        self.values_known = np.resize(self.true_values, self.l * self.w) # Список известных значений клеток

    # Подготовка данных при загрузке из файла
    def prepare_data(self):
        # Подготовка дополнительсных данных
        self.true_values_mas = list(np.resize(self.true_values, self.l * self.w)) # Список значений клеток
        self.status_mas = list(np.resize(self.status, self.l * self.w)) # Список статусов клеток
        self.values_known = list(np.resize(self.true_values, self.l * self.w)) # Список известных значений клеток

        # Установка метки для закрытых клеток поля
        for i in range(len(self.status_mas)):
            if(not self.status_mas[i]):
                self.values_known[i] = -10
    ##########

    ##########
    ### Преобразование данных
    # Преобразование x в матрицу
    def matrix_x(self):
        x = []
        for i in range(len(self.x)):
            x.append(np.resize(self.x[i], (self.l, self.w)))

        return x

    # Преобразование переменной matrix_values_known в матрицу
    def matrix_values_known(self):
        return np.resize(self.values_known, (self.l, self.w))

    # Преобразование координаты в число
    def coords_to_number(self, coordinates):
        return coordinates[0] * self.l + coordinates[1]

    # Преобразование число в координаты
    def number_to_coords(self, number):
        result = []
        result.append(math.floor(number / self.w))
        result.append(number % self.w)

        return result

    # Преобразование списка координат в список чисел
    def coords_list_to_numbers_list(self, coords_list):
        result = []
        for i in range(len(coords_list)):
            result.append(self.coords_to_number(coords_list[i]))

        return result

    # Преобразование списка чисел в список координат
    def numbers_list_to_coords_list(self, numbers_list):
        result = []
        for i in range(len(numbers_list)):
            result.append(self.number_to_coords(numbers_list[i]))
    ##########

    ##########
    ### Работа с соседними клетками
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

    # Получить список номеров соседних клеток по номеру
    def get_near_values_on_number(self, number):
        coords = self.number_to_coords(number)
        result = self.get_near_values_on_coords(coords)

        result1 = []
        for i in range(len(result)):
            result1.append(self.coords_to_number(result[i]))

        return result1

    # Получить список соседних закрытых клеток по номеру (уравнение)
    def get_near_close(self, number):
        c = self.number_to_coords(number)
        result = self.get_near_values_on_coords(c[0], c[1])

        result1 = []
        for i in range(len(result)):
            if((self.status[result[i][0]][result[i][1]] == False) and (self.values_known[self.coords_to_number(result[i])] != -1)):
                result1.append(result[i])
        result2 = self.coords_list_to_numbers_list(result1)

        list_x = np.zeros(self.l * self.w)
        for i in range(len(result2)):
            list_x[result2[i]] = 1

        return list_x

    # Получить количество найденных мин в соседних клетках по номеру
    def get_near_mines(self, number):
        near = self.get_near_values_on_number(number)

        counter = 0
        for i in range(len(near)):
            if(self.values_known[near[i]] == -1):
                counter = counter + 1

        return counter
    ##########

    ##########
    ### Работа с системой уравнений
    # Создание системы уравнений и базовая обработка
    def create_system(self):
        # Получение списков с соседними клетками (получение матрицы x)
        for i in range(self.l):
            for j in range(self.w):
                helper_unknown = list(np.zeros((self.l, self.w)))

                result = self.get_near_values_on_coords(i, j)
                for k in range(len(result)):
                    if(not self.status[result[k][0]][result[k][1]]):
                        helper_unknown[result[k][0]][result[k][1]] = 1

                helper_unknown1 = list(np.resize(helper_unknown, self.l * self.w))
                self.x.append(helper_unknown1)

        # Получение вектора y
        # self.y = copy.copy(self.true_values_mas)
        self.y = copy.copy(self.values_known)

        # Удаляем строки, где значение y[i] неизвестно (клетка закрыта)
        rows = []
        for i in range(len(self.status_mas)):
            if(not self.status_mas[i]):
                rows.append(i)

        x1 = list(np.delete(self.x, rows, axis=0))
        y1 = list(np.delete(self.y, rows))

        # Удаляем равенства из системы
        helper_mas = list(np.zeros(self.l * self.w))
        zeros_counter = collections.Counter(helper_mas)
        rows = []
        for i in range(len(y1)):
            if(collections.Counter(x1[i]) == zeros_counter):
                rows.append(i)

        if(len(rows) != 0):
            x2 = list(np.delete(x1, rows, axis=0))
            y2 = list(np.delete(y1, rows))

        self.x = copy.copy(x2)
        self.y = copy.copy(y2)

    # Удаление из системы уравнений уравнения с заданным номером
    def delete_equals(self, n):
        mas_n = [n]
        x1 = list(np.delete(self.x, mas_n, axis=0))
        y1 = list(np.delete(self.y, mas_n))

        self.x = copy.copy(x1)
        self.y = copy.copy(y1)

        print('Удалено уравнение №', n)
        print('Обновлённый x = ')
        print(self.matrix_x())
        print('Обновлённый y = ', self.y)

    # Добавление уравнения в систему уравнений по списку номеров
    def add_equals(self, mas):
        for i in range(len(mas)):
            if(self.true_values_mas[mas[i]] == 0):
                # Открыть все соседние клетки
                # Получаем список номеров соседних клеток
                near_numbers = self.get_near_values_on_number(mas[i])

                # Открыть все соседние клетки
                for j in range(len(near_numbers)):
                    self.opening_cell(near_numbers[j])

            elif(not self.true_values_mas[mas[i]] - self.get_near_mines(mas[i]) == 0):


    # Открытие клетки
    def opening_cell(self, number):
        self.values_known[number] = self.true_values_mas[number]
        self.status_mas[number] = True
        self.status[self.number_to_coords(number)[0]][self.number_to_coords(number)[1]] = True
    ##########

    ##########
    ### Реализация методов решения системы уравнений
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

            if((self.y[i] == 0) and (len(helper_mas) == 0)):
                print('Путь 1')
                changes = True
                self.delete_equals(i)
                break
            elif((self.y[i] == 0) and (len(helper_mas) > 0)):
                print('Путь 2')
                changes = True

                # Открываем клетки
                for k in range(len(helper_mas)):
                    self.opening_cell(helper_mas[k])

                for k in range(len(helper_mas)):
                    for i1 in range(len(self.x)):
                        self.x[i1][helper_mas[k]] = 0

                for k in range(len(helper_mas)):
                    if(collections.Counter(self.get_near_close(helper_mas[k])) != collections.Counter(np.zeros(self.l * self.w))):
                        print('Добавлено уравнение')
                        print('y = ', self.values_known[helper_mas[k]])
                        print('x = ')
                        print(np.resize(self.get_near_close(helper_mas[k]), (self.l, self.w)))

                        self.y.append(self.values_known[helper_mas[k]])
                        self.x.append(self.get_near_close(helper_mas[k]))

                        print('Обновлённый x = ')
                        print(self.matrix_x())
                        print('Обновлённый y = ', self.y)

                self.delete_equals(i)
                break
            elif(counter == self.y[i]):
                print('Путь 3')
                changes = True
                for k in range(len(helper_mas)):
                    self.values_known[helper_mas[k]] = -1
                    for i1 in range(len(self.x)):
                        if(self.x[i1][helper_mas[k]] == 1):
                            self.x[i1][helper_mas[k]] = 0
                            self.y[i1] = self.y[i1] - 1
                self.delete_equals(i)
                break
        return changes
    ##########

if __name__ == "__main__":
    my_minesweeper = Minesweeper()

    my_minesweeper.load_data()
    my_minesweeper.create_system()

    counter = 0
    while(len(my_minesweeper.x) != 0):
        result = my_minesweeper.method1()
        counter = counter + 1

    print(my_minesweeper.matrix_values_known())