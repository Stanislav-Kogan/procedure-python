list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
players_count = len(list_players)
team_1 = list_players[:players_count//2]
team_2 = list_players[players_count//2:]

print(team_1)
print(team_2)