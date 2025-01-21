# тема "Режимы открытия файлов"
class Product:
    def __init__(self, name, weight, category):
        self.name = name #  название продукта
        self.weight = weight # общий вес товара
        self.category = category # категория товара

    def __str__(self):
        """Возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены запятой с пробелами."""
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        """Инкапсулированный атрибут"""
        self.__file_name = 'products.txt'

    def get_products(self):
        """Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает
        единую строку со всеми товарами из файла __file_name."""
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ''

    def add(self, *products):
        """Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
        Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
        Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'"""
        current_products = self.get_products()
        current_product_names = {line.split(', ')[0] for line in current_products.split('\n') if line}

        new_entries = []
        for product in products:
            if product.name in current_product_names:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                new_entries.append(str(product))

        if new_entries:
            with open(self.__file_name, 'a') as file:
                for entry in new_entries:
                    file.write(entry + '\n')
                current_product_names.update({entry.split(', ')[0] for entry in new_entries})


# Пример использования
s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)
print(s1.get_products())
