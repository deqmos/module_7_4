import os
import time

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.startswith('.') or file.endswith('.pyc'): # У меня было ошибка связанная с отсутствием одного файла с расширением .pyc
            continue
        filepath = os.path.join(file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(root).split('\\')[-1]
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
