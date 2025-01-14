import random


# класс описывающий животных.
class Animal:
    live = True
    sound = None  # звук
    _DEGREE_OF_DANGER = 0 # степень опасности существа

    def __init__(self, speed):
        if speed is None or not isinstance(speed, (int, float)) or speed <= 0:
            raise ValueError("Скорость должна быть положительным числом.")
        self._cords = [0, 0, 0] # координаты в пространстве
        self.speed = speed #  скорость передвижения существа

    def move(self, dx, dy, dz):
        """Который должен менять соответствующие координаты в _cords на dx, dy и dz
        в том же порядке, где множетелем будет являться speed. Если при попытке изменения
        координаты z в _cords значение будет меньше 0, то выводить сообщение "It's too deep,
        i can't dive :(", при этом изменения не вносяться."""
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += new_z


    def get_cords(self):
        """Который выводит координаты в формате: X: <координаты по x>, Y:
        <координаты по y>, Z: <координаты по z>"""
        print(f'X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}')

    def attack(self):
        """который выводит "Sorry, i'm peaceful :)", если степень опасности
        меньше 5 и "Be careful, i'm attacking you 0_0" , если равно или больше."""
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        """Который выводит строку со звуком sound."""
        if self.sound:
            print(self.sound)
        else:
            print("...")


# класс описывающий птиц.
class Bird:
    beak = True # наличие клюва

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f'Here are(is) {eggs} eggs for you')


# класс описывающий плавающего животного
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        """- где dz изменение координаты z в _cords. Этот метод должен всегда
        уменьшать координату z в _coords. Чтобы сделать dz положительным,
        берите его значение по модулю (функция abs). Скорость движения при нырянии
        должна уменьшаться в 2 раза, в отличие от обычного движения. (speed / 2)"""
        dz = abs(dz)
        new_z = self._cords[2] - dz * (self.speed / 2)
        if new_z < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[2] = new_z

# класс описывающий ядовитых животных
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

# класс описывающий утконоса
class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click" # звук, который издаёт утконос

    def __init__(self, speed):
        super().__init__(speed)


# Пример работы программы:
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(3)
db.get_cords()
db.lay_eggs()

