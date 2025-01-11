class Animal:
    def __init__(self, name):
        self.name = name # Индивидуальное название каждого животного
        self.alive = True # Живой
        self.fed = False # Накормленный

    def eat(self, food):
        """Метод для еды, проверяет съедобность растения."""
        if isinstance(food, Plant) : # Проверяем, является ли food растением
            if food.edible: # Если растение съедобное
                self.fed = True
                print(f'{self.name} съел {food.name}')
            else: # Если растение несъедобное
                self.alive = False
                print(f'{self.name} не стал есть {food.name} и погиб')
        else:
            print('Это не растение')


class Plant:
    def __init__(self, name, edible = False):
        self.edible = edible # съедобность
        self.name = name # Индивидуальное название каждого растения


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, edible=True)


# Пример результата выполнения программы:
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)