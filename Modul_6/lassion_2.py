class Vehicle: # это любой транспорт
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white'] # список допустимых цветов для окрашивания

    def __init__(self, owner, model: str, color: str, engine_power: int):
        self.owner = owner # владелец транспорта
        self.__model = model # модель (марка) транспорта
        self.__engine_power = engine_power # мощность двигателя
        self.__color = self.__validate_color(color) # Устанавливаем цвет после проверки

    def __validate_color(self, color):
        """Проверка, что цвет допустим"""
        if color.lower() in self.__COLOR_VARIANTS:
            return color.capitalize()
        raise ValueError(f"Недопустимый цвет '{color}'. Возможные варианты: {', '.join(self.__COLOR_VARIANTS)}")


    def get_model(self):
        """Возвращает модель транспорта"""
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        """Возвращает мощность двигателя"""
        return f'Мощность двигателя: {self.__engine_power} л.с.'

    def get_color(self):
        """Возвращает цвет транспорта"""
        return f'Цвет: {self.__color}'

    def chang_owner(self, new_owner):
        """Изменение владельца транспорта"""
        self.owner = new_owner
        print(f"Теперь владелец транспорта: {self.owner}")

    def  print_info(self):
        """Распечатывает результаты методов (в том же порядке):
        get_model, get_horsepower, get_color; а так же владельца в конце в формате "Владелец: <имя>"."""
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        """Принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в
        списке __COLOR_VARIANTS, в противном случае выводит на экран надпись:
        Нельзя сменить цвет на <новый цвет>"."""
        if self.__color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 # в седан может поместиться только 5 пассажиров

    def get_passengers_limin(self):
        # Возвращает лимит пассажиров для седана
        return f'Лимит пассажиров: {self.__PASSENGERS_LIMIT}'


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()