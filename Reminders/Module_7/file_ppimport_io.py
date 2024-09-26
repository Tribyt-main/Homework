import io
from pprint import pprint

name = 'sample.txt'
file = open(name, 'r')
pprint(file.tell()) #Проверка курсорa
# pprint(file.seek(0)) #Смещение курсора
print(file.closed)
print(file.writable()) #Методы проверки файла.
print(file.readable())
print(file.seekable())
pprint(file.read())
file.close()