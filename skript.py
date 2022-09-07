import json


def func():
    with open('Table.csv', 'r') as f: # Открытие файла в режиме чтения.

        lines = []
        for line in f.readlines():
            lines.append(line.rstrip().split(',')) # Добавление всех строк файла без переносов строки.

        keys = lines[0]
        value = []

        for i in range(1, len(lines)): # Цикл, выполняемый столько раз, сколько есть элементов в списке "lines" -1.
            Dictionary = zip(keys, lines[i]) # Объединение 2 объектов в один кортеж.
            value.append(dict(Dictionary)) # Добавление кортежа в список, с последующим превращением его в словарь.

        with open("data.file.json", "w") as write_file: # Создание нового файла формата .json, открытие его в режиме изменения.
            json.dump(value, write_file) # Сохранение полученной информации в данном файле.

        return value


def main(): 
    func()


if __name__ == "__main__":
    main()
            