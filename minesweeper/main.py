import csv
import os
import minesweeper

class Menu:
    def __init__(self):
        self.fields = [] # Список экземпляров класса Minesweeper

        self.fields_path = "fields" # Путь к директории, где хранятся данные о поле

        self.fields_values = [] # Список путей к значениям полей
        self.fields_status = [] # Список путей к статусам клеток поля
        self.fields_info = [] # Список путей к информации о поле

    # Получаем полные значения путей к файлам полей
    def get_filenames(self, directory):
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                if(filename == 'values.csv'):
                    self.fields_values.append(os.path.join(dirpath, filename))
                elif(filename == 'status.csv'):
                    self.fields_status.append(os.path.join(dirpath, filename))
                elif(filename == 'field_info.csv'):
                    self.fields_info.append(os.path.join(dirpath, filename))

            for dirname in dirnames:
                self.get_filenames(dirname)

    # Загрузка данных о полях
    def load_fields(self):
        # Сохраняем в переменную путь к директории с полями
        path = os.path.join(os.getcwd(), self.fields_path)

        # Сохраняем пути к полям в список
        self.get_filenames(path)

        print(self.fields_values)
        print(self.fields_status)
        print(self.fields_info)

        for i in range(len(self.fields_values)):
            my_minesweeper = minesweeper.Minesweeper()

            with open(self.fields_values[i], 'r') as my_file:
                my_file = csv.reader(my_file, delimiter = ",")
                for row in my_file:
                    true_values = []
                    for j in range(len(row)):
                        true_values.append(int(row[j]))

                    my_minesweeper.true_values.append(true_values)

            with open(self.fields_status[i], 'r') as my_file:
                my_file = csv.reader(my_file, delimiter = ",")
                for row in my_file:
                    status = []
                    for j in range(len(row)):
                        if(row[j] == 'T'):
                            status.append(True)
                        elif(row[j] == 'F'):
                            status.append(False)

                    my_minesweeper.status.append(status)

            with open(self.fields_info[i], 'r') as my_file:
                my_file = csv.reader(my_file, delimiter = ",")
                for row in my_file:
                    my_minesweeper.l = int(row[0])
                    my_minesweeper.w = int(row[1])
                    my_minesweeper.count_of_mines = int(row[2])

            self.fields.append(my_minesweeper)

if __name__ == "__main__":
    my_menu = Menu()
    my_menu.load_fields()

    ###
    my_menu.fields[2].prepare_data()
    my_menu.fields[2].create_system()

    counter = 0
    while (len(my_menu.fields[2].x) != 0):
        print('Step = ', counter)
        print(my_menu.fields[2].matrix_x())
        print(my_menu.fields[2].y)
        print(my_menu.fields[2].matrix_values_known())

        result = my_menu.fields[2].method1()
        if(not result):
            break
        counter = counter + 1
    ###

    '''
    for i in range(len(my_menu.fields)):
        my_menu.fields[i].load_add_data()
        my_menu.fields[i].get_values_known()
        my_menu.fields[i].get_coords()
        my_menu.fields[i].get_near_values()
        my_menu.fields[i].cutting()

        counter = 0
        while (len(my_menu.fields[i].x) != 0):
            result = my_menu.fields[i].method1()
            counter = counter + 1

        print(my_menu.fields[i].matrix_values_known())
    '''