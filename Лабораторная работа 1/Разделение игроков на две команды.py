list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
nmembers = int(len(list_players)/2)
team1 = list_players[:nmembers]
team2 = list_players[nmembers:]
print(team1)
print(team2)
