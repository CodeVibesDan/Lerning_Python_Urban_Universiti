def add_everything_up(a, b):
    try:
        # Попытка сложить a и b (стандартное поведение Python)
        return a + b
    except TypeError:
        # Обработка ошибки, если a и b — разных типов
        return f"{a}{b}"  # Преобразуем оба аргумента в строки и соединяем их

# Примеры использования:
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))     # яблоко4215
print(add_everything_up(123.456, 7))         # 130.456