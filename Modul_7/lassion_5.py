# тема "Файлы в операционной системе"
import os
import time

# Определите каталог, по которому нужно пройти
directory = "."

# Пройдитесь по каталогу
for root, dirs, files in os.walk(directory):
    for file in files:
        # Сформируйте полный путь к файлу
        filepath = os.path.join(root, file)

        # Получите время последней модификации и отформатируйте его
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получить размер файла
        filesize = os.path.getsize(filepath)

        # Получите родительский каталог файла
        parent_dir = os.path.dirname(filepath)

        # Печать информации о файле
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
            f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
