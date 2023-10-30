users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

nvisits = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
nvisits["Общее количество"] = len(users)
nvisits["Уникальные посещения"] = len(set(users))

print(nvisits)
