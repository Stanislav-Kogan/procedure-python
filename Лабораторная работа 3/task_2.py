# TODO Напишите функцию find_common_participants
def find_common_participants(group_1, group_2, separator=','):
    list_1 = group_1.split(separator)
    list_2 = group_2.split(separator)
    set_1 = set(list_1)
    set_2 = set(list_2)
    intersect = set_1.intersection(set_2)
    return sorted(intersect)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
