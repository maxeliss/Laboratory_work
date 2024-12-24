# TODO Напишите функцию find_common_participants
def find_common_participans(first_group, second_group, separator=","):
    first_group_separator = set(first_group.split(separator))
    second_group_separator = set(second_group.split(separator))
    otvet = first_group_separator.intersection(second_group_separator)
    return otvet

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participans(participants_first_group, participants_second_group, '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
