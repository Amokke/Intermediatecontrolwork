import json
from sys import stdin

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

print("Работа с заметками\n Выберите действие: \n Чтение: 1\n Добавление: 2\n Редактирование: 2\n Удаление: 2\n")

