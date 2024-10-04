import os
import time


path = os.getcwd()
for root, dirs, files in os.walk(path):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.stat(file).st_size
        parent_dir = os.path.dirname(filepath)
        print(f' Обнаружен файл: {file},'
              f'\n Путь: {filepath},'
              f'\n Размер: {filesize} байт,'
              f'\n Время изменения: {formatted_time},'
              f'\n Родительская директория: {parent_dir}')
