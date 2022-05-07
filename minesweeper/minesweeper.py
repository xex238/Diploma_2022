import numpy as np
import copy
import collections
import math


class Minesweeper:
    def __init__(self):
        ### Основные переменные класса
        self.l = 0  # Количество строк
        self.w = 0  # Количество столбцов
        self.count_of_mines = -1  # Количество мин на поле

        self.true_values = []  # Значения клеток в виде матрицы
        self.true_values_mas = []  # Список значений клеток

        self.status = []  # Статус клеток в виде матрицы
        self.status_mas = []  # Список статусов клеток

        self.values_known = []  # Список известных значений клеток

        self.x = []  # Значения x системы уравнений
        self.y = []  # Значения y системы уравнений
        self.equal_numbers = [] # Список номеров клеток для каждого уравнения

        ### Переменные для повыщения эффективности работы методов
        self.statistic_values = []
        self.statistic_counter = []

        ### Схемы
        # Список с мини-полями
        self.schemes = set()

    ##########
    ### Работа с исходными данными
    # Получаение копии класса
    def get_copy(self, my_minesweeper):
        self.l = copy.copy(my_minesweeper.l)  # Количество строк
        self.w = copy.copy(my_minesweeper.w)  # Количество столбцов
        self.count_of_mines = copy.copy(my_minesweeper.count_of_mines)  # Количество мин на поле

        self.true_values = copy.copy(my_minesweeper.true_values)  # Значения клеток в виде матрицы
        self.true_values_mas = copy.copy(my_minesweeper.true_values_mas)  # Список значений клеток

        self.status = copy.copy(my_minesweeper.status)  # Статус клеток в виде матрицы
        self.status_mas = copy.copy(my_minesweeper.status_mas)  # Список статусов клеток

        self.values_known = copy.copy(my_minesweeper.values_known)  # Список известных значений клеток

        self.x = copy.copy(my_minesweeper.x)  # Значения x системы уравнений
        self.y = copy.copy(my_minesweeper.y)  # Значения y системы уравнений
        self.equal_numbers = copy.copy(my_minesweeper.equal_numbers)

    # Загрузка тестовых данных
    def load_data(self):
        self.l = 5  # Количество строк
        self.w = 5  # Количество столбцов
        self.count_of_mines = 3  # Количество мин на поле
        # Значения клеток в виде матрицы
        self.true_values = [[0, 0, 1, -1, 2], [0, 0, 1, 2, -1], [1, 1, 0, 1, 1], [-1, 1, 0, 0, 0], [1, 1, 0, 0, 0]]
        self.true_values_mas = np.resize(self.true_values, self.l * self.w)  # Список значений клеток
        # Статус клеток в виде матрицы
        self.status = [[True, True, True, False, False], [True, True, True, True, False],
                       [True, True, True, True, True], [False, True, True, True, True], [False, True, True, True, True]]
        self.status_mas = np.resize(self.status, self.l * self.w)  # Список статусов клеток

        self.values_known = np.resize(self.true_values, self.l * self.w)  # Список известных значений клеток

        for i in range(len(self.status_mas)):
            self.equal_numbers.append(i)

    # Подготовка данных при загрузке из файла
    def prepare_data(self):
        # Подготовка дополнительсных данных
        self.true_values_mas = list(np.resize(self.true_values, self.l * self.w))  # Список значений клеток
        self.status_mas = list(np.resize(self.status, self.l * self.w))  # Список статусов клеток
        self.values_known = list(np.resize(self.true_values, self.l * self.w))  # Список известных значений клеток

        # Установка метки для закрытых клеток поля
        for i in range(len(self.status_mas)):
            if (not self.status_mas[i]):
                self.values_known[i] = -10

        for i in range(len(self.status_mas)):
            self.equal_numbers.append(i)

    # Инициализация переменной для сбора статистики
    def init_statistics(self):
        for i1 in range(4):
            helper1 = []
            if(i1 != 1):
                for i2 in range(7):
                    helper2 = []
                    for i3 in range(2):
                        helper2.append([])
                    helper1.append(helper2)
            else:
                for i2 in range(10):
                    helper2 = []
                    for i3 in range(2):
                        helper2.append([])
                    helper1.append(helper2)
            self.statistic_values.append(helper1)

        self.statistic_counter = copy.copy(self.statistic_values)

    # Добавление значение в статистику
    def add_statistics(self, method, success, number1, number2=-1):
        criterias = []

        # Обработка и сбор статистики не для второго метода
        if((method != 2) or (number2 == -1)):
            # Сбор статистики
            criterias.append(len(self.get_near_on_number(number1)))
            criterias.append(len(self.get_near_close_on_number(number1)))
            criterias.append(self.get_count_near_mines_on_number(number1))
            position_near, position_near_close, position_near_mines = self.get_near_positions(number1)
            criterias.append(position_near)
            criterias.append(position_near_close)
            criterias.append(position_near_mines)
            criterias.append(self.values_known[number1])

            # Добавление собранной статистики в общую статистику
            for i in range(len(criterias)):
                if(criterias[i] not in self.statistic_values[method][i][success]):
                    self.statistic_values[method][i][success].append(criterias[i])
                    self.statistic_counter[method][i][success].append(1)
                else:
                    index = self.statistic_values[method][i][success].index(criterias[i])
                    self.statistic_counter[method][i][success][index] += 1
        # Обработка и сбор статистики для второго метода
        else:
            # Сбор статистики
            coords1 = self.number_to_coords(number1)
            coords2 = self.number_to_coords(number2)

            criterias.append(abs(coords1[0] - coords2[0]))
            criterias.append(abs(coords1[1] - coords2[1]))
            criterias.append(abs(self.values_known[number1] - self.values_known[number2]))

            criterias.append([len(self.get_near_on_number(number1)), len(self.get_near_on_number(number2))])
            criterias.append([len(self.get_near_close_on_number(number1)), len(self.get_near_close_on_number(number2))])
            criterias.append([self.get_count_near_mines_on_number(number1), self.get_count_near_mines_on_number(number2)])

            position_near1, position_near_close1, position_near_mines1 = self.get_near_positions(number1)
            position_near2, position_near_close2, position_near_mines2 = self.get_near_positions(number2)

            criterias.append([position_near1, position_near2])
            criterias.append([position_near_close1, position_near_close2])
            criterias.append([position_near_mines1, position_near_mines2])
            criterias.append([self.values_known[number1], self.values_known[number2]])

            # Добавление собранной статистики в общую статистику
            for i in range(3):
                if(criterias[i] not in self.statistic_values[method][i][success]):
                    self.statistic_values[method][i][success].append(criterias[i])
                    self.statistic_counter[method][i][success].append(1)
                else:
                    index = self.statistic_values[method][i][success].index(criterias[i])
                    self.statistic_counter[method][i][success][index] += 1

            for i in range(3, 10):
                for j in range(2):
                    if (criterias[i][j] not in self.statistic_values[method][i][success]):
                        self.statistic_values[method][i][success].append(criterias[i][j])
                        self.statistic_counter[method][i][success].append(1)
                    else:
                        index = self.statistic_values[method][i][success].index(criterias[i][j])
                        self.statistic_counter[method][i][success][index] += 1

    # Добавление схемы в список схем
    def add_scheme(self, numbers_list, values_list, true_number, true_value):
        min_i, min_j = self.get_min_coords(numbers_list)

        coords_list = self.numbers_list_to_coords_list(numbers_list)
        true_coords = self.number_to_coords(true_number)

        update_coords_list = []
        update_true_coords = [true_coords[0] - min_i, true_coords[1] - min_j]
        for i in range(len(coords_list)):
            update_coords_list.append([coords_list[i][0] - min_i, coords_list[i][1] - min_j])

        result_mas = [update_coords_list, values_list, update_true_coords, true_value]
        result_tuple = tuple(result_mas)

        if(result_tuple not in self.schemes):
            self.schemes.add(result_tuple)
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
    # Получить расположение соседних клеток (обычных, закрытых, с выявленными минами)
    def get_near_positions(self, number):
        coords = self.number_to_coords(number)
        near_coords = self.get_near_on_coords(coords[0], coords[1])
        near_numbers = self.coords_list_to_numbers_list(near_coords)

        near = np.zeros((3, 3))
        near_close = np.zeros((3, 3))
        near_mines = np.zeros((3, 3))

        for k in range(len(near_coords)):
            i = coords[0] - near_coords[k][0]
            j = coords[1] - near_coords[k][1]
            near[1 + i][1 + j] = 1

            if(not self.status_mas[near_numbers[k]]):
                near_close[1 + i][1 + j] = 1
            if(self.values_known[near_numbers[k] == -1]):
                near_mines[1 + i][1 + j] = 1

        return near, near_close, near_mines

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
            if (not self.status_mas[near[i]]):
                near_close.append(near[i])

        return near_close

    # Получить уравнение по номеру
    def get_equal(self, number):
        c = self.number_to_coords(number)  # Получаем координату по номеру
        coords_near = self.get_near_on_coords(c[0], c[1])  # Получаем координаты соседних клеток по координате

        # Получаем список координат соседних закрытых клеток без флага мины
        coords_x = []
        mines_counter = 0
        for i in range(len(coords_near)):
            if ((self.status[coords_near[i][0]][coords_near[i][1]] == False) and (self.values_known[self.coords_to_number(coords_near[i])] != -1)):
                coords_x.append(coords_near[i])
            if (self.values_known[self.coords_to_number(coords_near[i])] == -1):
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
    def get_count_near_mines_on_number(self, number):
        near = self.get_near_on_number(number)

        counter = 0
        for i in range(len(near)):
            if (self.values_known[near[i]] == -1):
                counter = counter + 1

        return counter

    # Получить минимальное значение координат (i, j) по номерам клеток
    def get_min_coords(self, numbers_list):
        min_i = self.l - 1
        min_j = self.w - 1

        for i in range(len(numbers_list)):
            coords = self.number_to_coords(numbers_list[i])
            near_coords = self.get_near_on_coords(coords[0], coords[1])
            for j in range(len(near_coords)):
                if(near_coords[i][0] < min_i):
                    min_i = near_coords[i][0]
                if(near_coords[i][1] < min_j):
                    min_j = near_coords[i][1]

        return min_i, min_j

    # Установить значение - в клетке нет мины
    def set_no_mine(self, mas_numbers_ones, caution=False):
        # Открываем клетки
        for k in range(len(mas_numbers_ones)):
            self.opening_cell(mas_numbers_ones[k], caution=caution)

        # Обнуляем соответствующие столбцы матрицы
        for k in range(len(mas_numbers_ones)):
            for i1 in range(len(self.x)):
                self.x[i1][mas_numbers_ones[k]] = 0

        # Добавление уравнений в систему
        if(not caution):
            self.add_equals(mas_numbers_ones)

    # Установить значение - в клетке находится мина
    def set_mine(self, mas_numbers_ones):
        for k in range(len(mas_numbers_ones)):
            self.values_known[mas_numbers_ones[k]] = -1
            for i1 in range(len(self.x)):
                if (self.x[i1][mas_numbers_ones[k]] == 1):
                    self.x[i1][mas_numbers_ones[k]] = 0
                    self.y[i1] = self.y[i1] - 1
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
                    if (not self.status[result[k][0]][result[k][1]]):
                        helper_unknown[result[k][0]][result[k][1]] = 1

                helper_unknown1 = list(np.resize(helper_unknown, self.l * self.w))
                self.x.append(helper_unknown1)

        # Получение вектора y
        self.y = copy.copy(self.values_known)

        # Удаляем строки, где значение y[i] неизвестно (клетка закрыта)
        rows = []
        for i in range(len(self.status_mas)):
            if (not self.status_mas[i]):
                rows.append(i)

        x1 = list(np.delete(self.x, rows, axis=0))
        y1 = list(np.delete(self.y, rows))
        equal_numbers1 = list(np.delete(self.equal_numbers, rows))

        # Удаляем равенства из системы
        helper_mas = list(np.zeros(self.l * self.w))
        zeros_counter = collections.Counter(helper_mas)
        rows = []
        for i in range(len(y1)):
            if (collections.Counter(x1[i]) == zeros_counter):
                rows.append(i)

        if (len(rows) != 0):
            x2 = list(np.delete(x1, rows, axis=0))
            y2 = list(np.delete(y1, rows))
            equal_numbers2 = list(np.delete(equal_numbers1, rows))

        self.x = copy.copy(x2)
        self.y = copy.copy(y2)
        self.equal_numbers = copy.copy(equal_numbers2)

    # Удаление из системы уравнений уравнения с заданными номерами
    def delete_equals(self, n):
        mas_n = [n]
        x1 = list(np.delete(self.x, mas_n, axis=0))
        y1 = list(np.delete(self.y, mas_n))
        equal_numbers1 = list(np.delete(self.equal_numbers, mas_n))

        self.x = copy.copy(x1)
        self.y = copy.copy(y1)
        self.equal_numbers = copy.copy(equal_numbers1)

        '''
        print('Удалено уравнение №', n)
        print('Обновлённый x = ')
        print(self.matrix_x())
        print('Обновлённый y = ', self.y)
        '''

    # Добавление уравнения в систему уравнений по списку номеров
    def add_equals(self, mas):
        for i in range(len(mas)):
            if (self.true_values_mas[mas[i]] == 0):
                ### Открыть все соседние клетки
                # Получаем список номеров соседних закрытых клеток
                near_close = self.get_near_close_on_number(mas[i])

                # Открыть все соседние закрытые клетки
                for j in range(len(near_close)):
                    self.opening_cell(near_close[j])

                # print(self.matrix_values_known())

                # Для каждой соседней открываемой клетки применить текущий метод
                self.add_equals(near_close)
            else:
                x, y = self.get_equal(mas[i])

                if (collections.Counter(x) != collections.Counter(np.zeros(self.l * self.w))):
                    self.x.append(x)
                    self.y.append(y)
                    self.equal_numbers.append(mas[i])

                '''
                print('Добавлено уравнение для координаты ', self.number_to_coords(mas[i]))
                print('Обновлённый x = ')
                print(self.matrix_x())
                print('Обновлённый y = ', self.y)
                print(self.matrix_values_known())
                '''

    # Открытие клетки по заданному номеру
    def opening_cell(self, number, caution=False):
        if(not caution):
            self.values_known[number] = self.true_values_mas[number]
        self.status_mas[number] = True
        self.status[self.number_to_coords(number)[0]][self.number_to_coords(number)[1]] = True
    ##########

    ##########
    ### Реализация методов решения системы уравнений
    # Реализация метода 1 (однозначное вычисление значений в закрытых клетках)
    def method1(self, caution=False, correct_check=False, collect_schemes=False, collect_statistics=False):
        changes = False
        correct = True
        cell_number = -1

        # Проверка клеток на корректность
        if(correct_check):
            for i in range(len(self.values_known)):
                if(self.values_known[i] != -10 and self.values_known[i] != -1):
                    near_close_count = len(self.get_near_close_on_number(i))
                    near_mines_count = self.get_count_near_mines_on_number(i)

                    if((near_close_count < self.values_known[i]) or (near_mines_count > self.values_known[i])):
                        print('Клетка с координатами ', self.number_to_coords(self.equal_numbers[i]), ' некорректна!')
                        print(self.matrix_values_known())
                        correct = False
                        return changes, correct

        # Работа с системой уравнений
        for i in range(len(self.x)):
            ones_counter = 0
            mines_counter = self.get_count_near_mines_on_number(i)
            mas_numbers_ones = []

            # Определяем количество единиц в уравнении
            for j in range(len(self.x[i])):
                ones_counter = ones_counter + self.x[i][j]
                if (self.x[i][j] == 1):
                    mas_numbers_ones.append(j)

            # Если число в клетке 0 и количество соседних закрытых клеток 0, то просто удаляем уравнение из системы
            if ((self.y[i] == 0) and (len(mas_numbers_ones) == 0)):
                # print('Число в клетке 0. Количество соседних закрытых клеток 0')
                changes = True
                self.delete_equals(i)
                cell_number = self.equal_numbers[i]
                break
            # Если число в клетке 0, а количество соседних закрытых клеток без флага мины больше 0
            elif ((self.y[i] == 0) and (len(mas_numbers_ones) > 0)):
                # print('Число в клетке 0. Количество соседних закрытых клеток без флага мины больше 0')
                changes = True
                self.set_no_mine(mas_numbers_ones, caution=caution)
                self.delete_equals(i)
                cell_number = self.equal_numbers[i]
                break
            # Если число в клетке равно количеству соседних закрытых клеток
            elif (ones_counter == self.y[i]):
                # print('Число в клетке равно количеству соседних закрытых клеток')
                changes = True
                self.set_mine(mas_numbers_ones)
                self.delete_equals(i)
                cell_number = self.equal_numbers[i]
                break

        # Добавление схемы
        if(collect_schemes and changes):
            self.add_scheme([cell_number])

        # Сбор статистики
        if(collect_statistics and correct):
            self.add_statistics(1, changes, cell_number)

        return changes, correct

    # Реализация метода 2 (вычитание уравнений по их номеру в системе)
    def method2(self, equal1, equal2, collect_schemes=False, collect_statistics=False):
        result = False
        cell_number1 = self.equal_numbers[equal1]
        cell_number2 = self.equal_numbers[equal2]

        # Получение разности двух уравнений
        delta_x = []
        ones_numbers = []
        minus_ones_numbers = []
        for i in range(len(self.x[equal1])):
            delta = self.x[equal1][i] - self.x[equal2][i]
            delta_x.append(delta)
            if (delta == 1):
                ones_numbers.append(i)
            elif (delta == -1):
                minus_ones_numbers.append(i)
        delta_y = self.y[equal1] - self.y[equal2]

        # Проверка: возможно ли однозначно вычислить значения, исходя из разности уравнений?
        if (len(ones_numbers) == delta_y):
            result = True
        elif (len(minus_ones_numbers) == -delta_y):
            result = True

            helper = copy.copy(ones_numbers)
            ones_numbers = copy.copy(minus_ones_numbers)
            minus_ones_numbers = copy.copy(helper)

        # Если возможно, вычисляем значения клеток
        if (result):
            # Обозначаем клетки с минами
            self.set_mine(ones_numbers)

            # Обозначаем клетки без мин
            self.set_no_mine(minus_ones_numbers)

            # Удаление уравнений из системы
            if (equal1 < equal2):
                self.delete_equals(equal2)
                self.delete_equals(equal1)
            else:
                self.delete_equals(equal1)
                self.delete_equals(equal2)

        # Добавление схем
        if(result and collect_schemes):
            self.add_scheme([cell_number1, cell_number2])

        # Сбор статистики
        if(collect_statistics):
            self.add_statistics(2, result, cell_number1, number2=cell_number2)

        return result

    # Генератор уравнений для метода 2
    def get_equals_for_method2(self):
        result = False
        while(True):
            for i in range(len(self.x)):
                for j in range(i + 1, len(self.x)):
                    result = self.method2(i, j)
                    if(result):
                        break
                if(result):
                    break
            if(not result):
                break

    # Реализация метода 3 (вычитание уравнений с применением уравнения с суммой общего количества мин)
    def method3(self, equal):
        result = False

        # Получаем уравнение с общим количеством мин
        x = list(np.zeros(self.l * self.w))

        mines_counter = 0
        for i in range(len(self.values_known)):
            if (not self.status_mas[i]):
                if (self.values_known[i] != -1):
                    x[i] = 1
                else:
                    mines_counter = mines_counter + 1

        y = self.count_of_mines - mines_counter

        # Получение разности двух уравнений
        delta_x = []
        delta_y = 0
        delta = 0
        ones_numbers = []
        minus_ones_numbers = []
        for i in range(len(self.x[equal])):
            delta = x[i] - self.x[equal][i]
            delta_x.append(delta)
            if (delta == 1):
                ones_numbers.append(i)
            elif (delta == -1):
                minus_ones_numbers.append(i)
        delta_y = y - self.y[equal]

        if (len(ones_numbers) == delta_y):
            result = True
        elif (len(minus_ones_numbers) == -delta_y):
            result = True

            helper = copy.copy(ones_numbers)
            ones_numbers = copy.copy(minus_ones_numbers)
            minus_ones_numbers = copy.copy(helper)

        if (result):
            # Обозначаем клетки с минами
            self.set_mine(ones_numbers)

            # Обозначаем клетки без мин
            self.set_no_mine(minus_ones_numbers)

            # Удаление уравнения из системы
            self.delete_equals(equal)

        return result

    # Реализация метода 4 (метод гипотез)
    def method4(self, number, value):
        result = False

        # Создание копии поля
        copy_minesweeper = Minesweeper()
        copy_minesweeper.get_copy()

        # Подстановка значения в каждую переменную системы
        if (value == 1):
            copy_minesweeper.set_mine([number])
        elif (value == 0):
            copy_minesweeper.set_no_mine([number], caution=True)

        # Проверка гипотезы
        while (True):
            changes, correct = copy_minesweeper.method1(caution=True, correct_check=True)
            if ((not changes) or (not correct)):
                break

        # Если гипотеза принята
        if ((not changes) and (correct)):
            result = True
            if (value == 1):
                self.set_mine([number])
            elif (value == 0):
                self.set_no_mine([number])

        return result

    # Проверка правильности решения поля
    def check_result(self):
        result = True
        for i in range(len(self.true_values_mas)):
            if (self.true_values_mas[i] != self.values_known[i]):
                result = False
                break

        return result
    ##########


if __name__ == "__main__":
    my_minesweeper = Minesweeper()
    my_minesweeper.init_statistics()

    '''
    my_minesweeper = Minesweeper()

    my_minesweeper.load_data()
    my_minesweeper.create_system()

    counter = 0
    while (len(my_minesweeper.x) != 0):
        result, _ = my_minesweeper.method1()
        counter = counter + 1

    print(my_minesweeper.matrix_values_known())
    '''