# TODO импортировать необходимые молули
from collections import OrderedDict
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
INDENT = 4

def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as inp:
        data_dict = list(csv.DictReader(inp))
    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as outp:
        json.dump(data_dict, outp, indent=INDENT)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
