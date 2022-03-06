# Метод для создания базовых схем (схем из базовых правил)
def get_base_schemes(self, main_menu):
    bool_mas = [True, False]
    for number in range(8):  # Цифру 0 не трогаем
        for i1 in range(2):
            for i2 in range(2):
                for i3 in range(2):
                    for i4 in range(2):
                        for i5 in range(2):
                            for i6 in range(2):
                                for i7 in range(2):
                                    for i8 in range(2):
                                        i = [0, 0, 0, 1, 1, 2, 2, 2]
                                        j = [0, 1, 2, 0, 2, 0, 1, 2]
                                        is_mine = [bool_mas[i1], bool_mas[i2], bool_mas[i3], bool_mas[i4], bool_mas[i5],
                                                   bool_mas[i6], bool_mas[i7], bool_mas[i8]]
                                        result = Rule.check_rule_easy(number + 1, is_mine)

                                        my_scheme = Scheme()
                                        input = []
                                        for k in range(len(i)):
                                            input.append(True_point(i[k], j[k], is_mine[k]))

# Класс для проверки соседних клеток по базовым правилам
class Rule:
    def __init__(self):
        self.input = [] # Входные данные (экземпляры классы Point/True_point)

    def __init__(self, input):
        self.input = input

    # Проверка базового правила: если количество мин вокруг цифры равно данной цифре, то правило верное
    def check_rule(self, number):
        mine_counter = 0
        for i in range(len(self.input)):
            if(self.input[i].value == -1):
                mine_counter = mine_counter + 1

        if(mine_counter == number):
            return True
        else:
            return False

    # Проверка базового правила только при boolean-значении value экземпляра True_point
    def check_rule_easy(number, values):
        mine_counter = 0
        for i in range(len(values)):
            if(values[i] == True):
                mine_counter = mine_counter + 1

        if(mine_counter == number):
            return True
        else:
            return False

    # Логические правила о прогнозировании значений закрытых клеток (для поля 3*3)
    def logic_rule(self, number):
        mine_counter = 0
        close_cell_counter = 0
        for i in range(len(self.input)):
            if(self.input[i].mark_mine):
                mine_counter = mine_counter + 1
            if(not self.input[i].is_open):
                close_cell_counter = close_cell_counter + 1

# Данные по связям между клетками (в которых однозначно есть N мин)
class Connection:
    def __init__(self):
        self.points_i = None
        self.points_j = None
        self.count_of_points = None # int - Количество точек в связке (len(points))
        self.count_of_mines = None # int - Количество мин в связанных клетках

