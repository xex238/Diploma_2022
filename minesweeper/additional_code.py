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