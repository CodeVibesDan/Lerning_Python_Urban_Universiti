# тема "Позиционирование в файле"
def custom_write(file_name, strings):
    """Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла
     для записи, strings - список строк для записи."""
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            position = file.tell()
            file.write(string + '\n')
            strings_positions[(line_number, position)] = string

    return strings_positions


# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
