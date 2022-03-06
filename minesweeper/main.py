import os
import json

# Класс для хранения схем
class Scheme:
    def __init__(self):
        self.input = [] # Входные данные (экземпляры класса True_point)
        self.output = None # Выходные данных (экземпляр класса True_point)

        '''
        Тип схемы
        - 'bool': схема 'есть мина или нет'
        - 'number' схема с числами
        '''
        self.type = None

    def __init__(self, input, output, type):
        self.input = input
        self.output = output
        self.type = type

# Класс с истинными значениями для клетки
class True_point:
    def __int__(self):
        self.i = None # i-координата клетки
        self.j = None # j-координата клетки
        self.value = None # int [-1; 8] - Значение в клетке

    def __init__(self, i, j, value):
        self.i = i
        self.j = j
        self.value = value

# Данные по каждой координате
class Point:
    def __init__(self):
        self.i = None # i-координата клетки
        self.j = None # j-координата клетки
        self.value = None # int [-1; 8] - Значение в клетке (если клетка открыта, иначе None)
        self.probability = None # float - Вероятность того, что в клетке находится мина (если клетка закрыта, иначе None)
        self.is_open = None # bool - Открыта ли клетка
        self.p1 = [] # Матрица (3; 3) с вероятностями нахождения мины в соседних клетках
        self.true_point = None # Экземпляр класса True_point
        self.mark_mine = False # Метка мины. Стоит ли флаг мины в данной клетке
        self.type = None # Вид/тип ячейки

# Данные по полю
class Field:
    def __init__(self):
        self.length = None # int - Длина поля
        self.width = None # int - Ширина поля
        self.total_count_of_mines = None # int - Общее количество мин на поле
        self.count_of_mines = 0 # int - Текущее количество мин на поле
        self.points = [] # Матрица (length; width) экземпляров класса Point
        self.connections = [] # Список экземпляров класса Connection

    # Расчёт количества значений mark_mine = True в соседних клетках
    def min_mines(self, i, j):
        adjacent_cells = self.get_adjacent_cells(i, j)
        counter = 0

        for i in range(len(adjacent_cells)):
            if(adjacent_cells[i].mark_mine):
                counter = counter + 1

        return counter

    # Расчёт количества значений is_open = False в соседних клетках
    def max_mines(self, i, j):
        adjacent_cells = self.get_adjacent_cells(i, j)
        counter = 0

        for i in range(len(adjacent_cells)):
            if(not adjacent_cells[i].is_open):
                counter = counter + 1

        return counter

    # Проверка правильности ситуации: если количество соседних закрытых клеток меньше, чем число в клетке, то ситуация неверная
    def is_correct_situation(self, i, j):
        count_close_points = self.max_mines(i, j)
        number = self.points[i][j].value
        if(count_close_points < number):
            return False
        else:
            return True

    # Получить список координат соседних клеток и их количество
    def get_adjacent_cells(self, i, j):
        adjacent_cells = []
        counter = 0

        if((i == 0) and (j == 0)):
            adjacent_cells.append(self.points[i][j + 1])
            adjacent_cells.append(self.points[i + 1][j + 1])
            adjacent_cells.append(self.points[i + 1][j])
            counter = 3
        elif((i == 0) and ((j != 0) or (j != self.length))):
            adjacent_cells.append(self.points[i][j + 1])
            adjacent_cells.append(self.points[i + 1][j + 1])
            adjacent_cells.append(self.points[i + 1][j])
            adjacent_cells.append(self.points[i + 1][j - 1])
            adjacent_cells.append(self.points[i][j - 1])
            counter = 5
        elif((i == 0) and (j == self.length)):
            adjacent_cells.append(self.points[i + 1][j])
            adjacent_cells.append(self.points[i + 1][j - 1])
            adjacent_cells.append(self.points[i][j - 1])
            counter = 3
        elif(((i != 0) or (i != self.width)) and (j == self.length)):
            adjacent_cells.append(self.points[i + 1][j])
            adjacent_cells.append(self.points[i - 1][j - 1])
            adjacent_cells.append(self.points[i][j - 1])
            adjacent_cells.append(self.points[i - 1][j - 1])
            adjacent_cells.append(self.points[i - 1][j])
            counter = 5
        elif((i == self.width) and (j == self.length)):
            adjacent_cells.append(self.points[i][j - 1])
            adjacent_cells.append(self.points[i - 1][j - 1])
            adjacent_cells.append(self.points[i - 1][j])
            counter = 3
        elif((i == self.width) and ((j != self.length) or (j != 0))):
            adjacent_cells.append(self.points[i][j - 1])
            adjacent_cells.append(self.points[i - 1][j - 1])
            adjacent_cells.append(self.points[i - 1][j])
            adjacent_cells.append(self.points[i - 1][j + 1])
            adjacent_cells.append(self.points[i][j + 1])
            counter = 5
        elif((i == self.width) and (j == 0)):
            adjacent_cells.append(self.points[i - 1][j])
            adjacent_cells.append(self.points[i - 1][j + 1])
            adjacent_cells.append(self.points[i][j + 1])
            counter = 3
        elif(((i != self.width) or (i != 0)) and (j == 0)):
            adjacent_cells.append(self.points[i - 1][j])
            adjacent_cells.append(self.points[i - 1][j + 1])
            adjacent_cells.append(self.points[i][j + 1])
            adjacent_cells.append(self.points[i + 1][j + 1])
            adjacent_cells.append(self.points[i + 1][j])
            counter = 5
        else:
            adjacent_cells.append(self.points[i - 1][j])
            adjacent_cells.append(self.points[i - 1][j + 1])
            adjacent_cells.append(self.points[i][j + 1])
            adjacent_cells.append(self.points[i + 1][j + 1])
            adjacent_cells.append(self.points[i + 1][j])
            adjacent_cells.append(self.points[i + 1][j - 1])
            adjacent_cells.append(self.points[i][j - 1])
            adjacent_cells.append(self.points[i - 1][j - 1])
            counter = 8

        return adjacent_cells, counter

# Данные по меню
class Menu:
    def __init__(self):
        self.fields = [] # Список экземпляров класса Point
        self.fields_path = "fields\\field_1" # str - Путь к директории, где хранятся данные о поле
        self.fields_filenames = [] # Список путей к данным о полях
        # self.base_rules = [] # Базовые правила
        # self.rules = [] # Производные правила
        self.schemes = [] # Схемы

    def init_base_rules(self):
        # Инициализация базового правила: вокруг цифры 1 должна быть 1 мина
        point = Point()

    # Загрузка данных о полях с json файлов
    def load_fieds_json(self):
        # Сохраняем в переменную путь к директории с полями
        path = os.path.join(os.getcwd(), self.fields_path)

        # Сохраняем пути к полям в список
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                self.fields_filenames.append(os.path.join(dirpath, filename))

        for i in range(len(self.fields_filenames)):
            with open(self.fields_filenames[i], "r") as file:
                data = json.load(file)

                my_field = Field()
                my_field.length = data['length']
                my_field.width = data['width']
                my_field.total_count_of_mines = data['total_count_of_mines']

                for point in data['points']:
                    my_point = Point()

                    my_point.true_point = True_point()
                    my_point.true_point.i = point['i']
                    my_point.true_point.j = point['j']
                    my_point.true_point.value = point['value']

                    my_point.i = point['i']
                    my_point.j = point['j']
                    my_point.is_open = point['is_open']
                    if(my_point.is_open):
                        my_point.value = point['value']

                    my_field.points.append(my_point)

                self.fields.append(my_field)

main_menu = Menu()
main_menu.load_fieds_json()