# Получить список номеров соседних клеток по номеру
def get_near_values_on_number(self, number):
    result = []
    coords = self.number_to_coords(number)
    if ((coords[0] == 0) and (coords[1] == 0)):
        result.append(self.coords_to_number(coords[0], coords[1] + 1))
        result.append(self.coords_to_number(coords[0] + 1, coords[1]))
        result.append(self.coords_to_number(coords[0] + 1, coords[1] + 1))
    elif ((coords[0] == 0) and ((coords[1] > 0) and (coords[1] < self.w - 1))):
        result.append(self.coords_to_number(coords[0], coords[1] - 1))
        result.append(self.coords_to_number(coords[0] + 1, coords[1] - 1))
        result.append(self.coords_to_number(coords[0] + 1, coords[1]))
        result.append(self.coords_to_number(coords[0] + 1, coords[1] + 1))
        result.append(self.coords_to_number(coords[0], coords[1] + 1))
    elif ((coords[0] == 0) and (coords[1] == self.w - 1)):
        result.append(self.coords_to_number(coords[0], coords[1] - 1))
        result.append(self.coords_to_number(coords[0] + 1, coords[1] - 1))
        result.append(self.coords_to_number(coords[0] + 1, coords[1]))
    elif (((coords[0] > 0) and (coords[0] < self.l - 1)) and (coords[1] == self.w - 1)):
        result.append(self.coords_to_number(coords[0] - 1, coords[1]))
        result.append(self.coords_to_number(coords[0] - 1, coords[1] - 1))
        result.append(self.coords_to_number(coords[0], coords[1] - 1))
        result.append(self.coords_to_number(coords[0] + 1, coords[1] - 1))
        result.append(self.coords_to_number(coords[0] + 1, coords[1]))
    elif ((coords[0] == self.l - 1) and (coords[1] == self.w - 1)):
        result.append(self.coords_to_number(coords[0] - 1, coords[1]))
        result.append(self.coords_to_number(coords[0] - 1, coords[1] - 1))
        result.append(self.coords_to_number(coords[0], coords[1] - 1))
    elif ((coords[0] == self.l - 1) and ((coords[1] > 0) and (coords[1] < self.w - 1))):
        result.append(self.coords_to_number(coords[0], coords[1] - 1))
        result.append(self.coords_to_number(coords[0] - 1, coords[1] - 1))
        result.append(self.coords_to_number(coords[0] - 1, coords[1]))
        result.append(self.coords_to_number(coords[0] - 1, coords[1] + 1))
        result.append(self.coords_to_number(coords[0], coords[1] + 1))
    elif ((coords[0] == self.l - 1) and (coords[1] == 0)):
        result.append(self.coords_to_number(coords[0] - 1, coords[1]))
        result.append(self.coords_to_number(coords[0] - 1, coords[1] + 1))
        result.append(self.coords_to_number(coords[0], coords[1] + 1))
    elif (((coords[0] > 0) and (coords[0] < self.l - 1)) and (coords[1] == 0)):
        result.append(self.coords_to_number(coords[0] - 1, coords[1]))
        result.append(self.coords_to_number(coords[0] - 1, coords[1] + 1))
        result.append(self.coords_to_number(coords[0], coords[1] + 1))
        result.append(self.coords_to_number(coords[0] + 1, coords[1] + 1))
        result.append(self.coords_to_number(coords[0] + 1, coords[1]))
    elif (((coords[0] > 0) and (coords[0] < self.l - 1)) and ((coords[1] > 0) and (coords[1] < self.w - 1))):
        result.append(self.coords_to_number(coords[0] - 1, coords[1] - 1))
        result.append(self.coords_to_number(coords[0] - 1, coords[1]))
        result.append(self.coords_to_number(coords[0] - 1, coords[1] + 1))
        result.append(self.coords_to_number(coords[0], coords[1] - 1))
        result.append(self.coords_to_number(coords[0], coords[1] + 1))
        result.append(self.coords_to_number(coords[0] + 1, coords[1] - 1))
        result.append(self.coords_to_number(coords[0] + 1, coords[1]))
        result.append(self.coords_to_number(coords[0] + 1, coords[1] + 1))

    return result

    # Добавление схемы в список схем
    def add_scheme(self, numbers_list, true_coords, true_value):
        coords_tuple = []

        coords_list = []
        values_list = []

        # Получить минимальное значение координат по номерам клеток
        min_i, min_j = self.get_min_coords(numbers_list)

        for i in range(len(numbers_list)):
            coords = self.number_to_coords(numbers_list[i])
            near_coords = self.get_near_on_coords(coords[0], coords[1])

            for j in range(len(near_coords)):
                number = self.coords_to_number(near_coords[j])
                value = self.values_known[number]

                if(near_coords[i] not in coords_list):
                    coords_list.append([near_coords[i][0] - min_i, near_coords[i][1] - min_j])
                    values_list.append(value)

        for i in range(len(coords_list)):
            coords_tuple.append(tuple(coords_list[i]))

        self.schemes.add(tuple(tuple(coords_tuple), tuple(values_list)))