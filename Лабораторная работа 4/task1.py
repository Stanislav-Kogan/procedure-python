# TODO решите задачу
import json

INPUT_FILENAME = 'input.json'
ROUNDING = 3

def task() -> float:
    with open(INPUT_FILENAME, 'r') as inp:
        data_dict = json.load(inp)
    data_list = [item["score"] * item["weight"] for item in data_dict]
    return round(sum(data_list), ROUNDING)

print(task())
