import json


def func():
    with open('Table.csv', 'r') as f: # Открытие файла в режиме чтения.

        lines = []
        value = []
        
        for line in f.readlines(): # Перебор всех строк в файле csv
            lines.append(line.rstrip().split(',')) # Добавление всех строк файла без переносов строки.
            if len(lines) <= 1: # Ограничение на выпонение функции зип, пока в списке не будет 2 элемента
                continue
            map(value.append(dict(zip(lines[0], lines[1]))), lines) # Объединение заглавного и второстепенного списка в словарь, с сохранением в список.
            del lines[1] # Удаление второстепенного списка.

            
        with open("data.file.json", "w") as write_file: # Создание нового файла формата .json, открытие его в режиме изменения.
            json.dump(value, write_file, indent=1) # Сохранение полученной информации в данном файле.
    return value


def main(): 
    print(func())


if __name__ == "__main__":
    main()
            