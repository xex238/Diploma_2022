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
    def get_near_on_coords(self, i, j):
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
    def get_near_on_number(self, number):
        coords = self.number_to_coords(number)
        result = self.get_near_on_coords(coords[0], coords[1])

        result1 = []
        for i in range(len(result)):
            result1.append(self.coords_to_number(result[i]))

        return result1

    # Получить список соседних закрытых клеток по номеру
    def get_near_close_on_number(self, number):
        near = self.get_near_on_number(number)

        near_close = []
        for i in range(len(near)):
            if(not self.status_mas[near[i]]):
                near_close.append(near[i])

        return near_close

    # Получить уравнение по номеру
    def get_equal(self, number):
        c = self.number_to_coords(number) # Получаем координату по номеру
        coords_near = self.get_near_on_coords(c[0], c[1]) # Получаем координаты соседних клеток по координате

        # Получаем список координат соседних закрытых клеток без флага мины
        ################### Получаем список координат соседних закрытых клеток
        coords_x = []
        mines_counter = 0
        for i in range(len(coords_near)):
            if((self.status[coords_near[i][0]][coords_near[i][1]] == False) and (self.values_known[self.coords_to_number(coords_near[i])] != -1)):
            # if (self.status[coords_near[i][0]][coords_near[i][1]] == False):
                coords_x.append(coords_near[i])
            if(self.values_known[self.coords_to_number(coords_near[i])] == -1):
                mines_counter = mines_counter + 1

        # Конвертируем список координат в список номеров
        numbers_x = self.coords_list_to_numbers_list(coords_x)

        # Конвертирование списка номеров в уравнение (x)
        x = np.zeros(self.l * self.w)
        for i in range(len(numbers_x)):
            x[numbers_x[i]] = 1

        # Получаем значение y за вычетом количества соседних клеток с флагом мины
        y = self.true_values_mas[number] - mines_counter

        return x, y

    # Получить количество найденных мин в соседних клетках по номеру
    def get_near_mines_on_number(self, number):
        near = self.get_near_on_number(number)

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

                result = self.get_near_on_coords(i, j)
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
                ### Открыть все соседние клетки
                # Получаем список номеров соседних закрытых клеток
                near_close = self.get_near_close_on_number(mas[i])

                # Открыть все соседние закрытые клетки
                for j in range(len(near_close)):
                    self.opening_cell(near_close[j])

                print(self.matrix_values_known())

                # Для каждой соседней открываемой клетки применить текущий метод
                self.add_equals(near_close)
            #elif(not self.true_values_mas[mas[i]] - self.get_near_mines_on_number(mas[i]) == 0):
            else:
                x, y = self.get_equal(mas[i])

                if (collections.Counter(x) != collections.Counter(np.zeros(self.l * self.w))):
                    self.x.append(x)
                    self.y.append(y)

                print('Добавлено уравнение для координаты ', self.number_to_coords(mas[i]))
                print('Обновлённый x = ')
                print(self.matrix_x())
                print('Обновлённый y = ', self.y)
                print(self.matrix_values_known())

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
            mas_numbers_ones = []

            # Определяем количество единиц в уравнении
            for j in range(len(self.x[i])):
                counter = counter + self.x[i][j]
                if(self.x[i][j] == 1):
                    mas_numbers_ones.append(j)

            # Если число в клетке 0 и количество соседних закрытых клеток 0, то просто удаляем уравнение из системы
            if((self.y[i] == 0) and (len(mas_numbers_ones) == 0)):
                print('Число в клетке 0. Количество соседних закрытых клеток 0')
                changes = True
                self.delete_equals(i)
                break
            # Если число в клетке 0, а количество соседних закрытых клеток без флага мины больше 0
            elif((self.y[i] == 0) and (len(mas_numbers_ones) > 0)):
                print('Число в клетке 0. Количество соседних закрытых клеток без флага мины больше 0')
                changes = True

                # Открываем клетки
                for k in range(len(mas_numbers_ones)):
                    self.opening_cell(mas_numbers_ones[k])

                # Обнуляем соответствующие столбцы матрицы
                for k in range(len(mas_numbers_ones)):
                    for i1 in range(len(self.x)):
                        self.x[i1][mas_numbers_ones[k]] = 0

                print(self.matrix_values_known())

                # Добавление уравнений в систему
                self.add_equals(mas_numbers_ones)

                '''
                for k in range(len(mas_numbers_ones)):
                    if(collections.Counter(self.get_equal(mas_numbers_ones[k])) != collections.Counter(np.zeros(self.l * self.w))):
                        print('Добавлено уравнение')
                        print('y = ', self.values_known[mas_numbers_ones[k]])
                        print('x = ')
                        print(np.resize(self.get_equal(mas_numbers_ones[k]), (self.l, self.w)))

                        self.y.append(self.values_known[mas_numbers_ones[k]])
                        self.x.append(self.get_equal(mas_numbers_ones[k]))

                        print('Обновлённый x = ')
                        print(self.matrix_x())
                        print('Обновлённый y = ', self.y)
                '''

                self.delete_equals(i)
                break
            # Если число в клетке равно количеству соседних закрытых клеток
            elif(counter == self.y[i]):
                print('Число в клетке равно количеству соседних закрытых клеток')
                changes = True
                for k in range(len(mas_numbers_ones)):
                    self.values_known[mas_numbers_ones[k]] = -1
                    for i1 in range(len(self.x)):
                        if(self.x[i1][mas_numbers_ones[k]] == 1):
                            self.x[i1][mas_numbers_ones[k]] = 0
                            self.y[i1] = self.y[i1] - 1
                self.delete_equals(i)
                break
        return changes
    ##########

    # Проверка правильности решения поля
    def check_result(self):
        result = True
        for i in range(len(self.true_values_mas)):
            if(self.true_values_mas[i] != self.values_known[i]):
                result = False
                break

        return result

if __name__ == "__main__":
    my_minesweeper = Minesweeper()

    my_minesweeper.load_data()
    my_minesweeper.create_system()

    counter = 0
    while(len(my_minesweeper.x) != 0):
        result = my_minesweeper.method1()
        counter = counter + 1

    print(my_minesweeper.matrix_values_known())