def find_common_participants(list1, list2, sep=','):
    participants_list1 = list1.split(sep)
    participants_list2 = list2.split(sep)

    common_participants = list(set(participants_list1).intersection(participants_list2))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
