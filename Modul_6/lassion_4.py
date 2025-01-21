import math

class Figure:
    """Родительский класс для фигур"""
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color) if self.__is_valid_color(*color) else [0,0,0]
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.filled = False

    def __is_valid_color(self, r, g, b):
        """Проверка корректности RGB-цвета"""
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        """Установка нового цвета (если корректный)"""
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Цвет указан некорректно.")

    def get_color(self):
        """Возвращает текущий цвет"""
        return self.__color

    def __is_valid_sides(self, *sides):
        """Проверка сторон на целые положительные числа"""
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def set_sides(self, *new_sides):
        """Изменение сторон (если корректное количество и значения)"""
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print("Стороны указаны некорректно или их количество не совпадает с sides_count.")

    def get_sides(self):
        """Возвращает список сторон"""
        return self.__sides

    def __len__(self):
        """Вычисляет периметр фигуры"""
        return sum(self.__sides)


class Cricle(Figure):
    """Класс окружности"""
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        """Вычисление площади круга"""
        return math.pi * self.__radius**2


class Triangle(Figure):
    """Класс треугольника"""
    sides_count = 3

    def get_square(self):
        """Вычисление площади треугольника (по формуле Герона)"""
        sides = self.get_sides()
        s = sum(sides) / 2  # Полупериметр
        return math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))


class Cube(Figure):
    """Класс куба"""
    sides_count = 12

    def __init__(self, color, *sides):
        side_length = sides[0] if len(sides) == 1 and sides[0] > 0 else 1
        super().__init__(color, *(side_length for _ in range(self.sides_count)))

    def get_volume(self):
        """Вычисление объёма куба"""
        side_length = self.get_sides()[0]
        return side_length**3


# Пример использования
circle1 = Cricle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]

cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # [6, 6, 6, ..., 6] (12 штук)

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Проверка периметра (длина окружности)
print(len(circle1))  # 15

# Проверка объёма (куба)
print(cube1.get_volume())  # 216