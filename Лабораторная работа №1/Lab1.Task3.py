# Разделение игроков на две команды
# Описание:
# У вас есть список players, который содержит имена игроков.
# Вам необходимо определить общее количество игроков в списке и затем с использованием слайсирования разделить игроков на две равные команды.
# Распечатайте каждую команду участников на отдельной строке.

list_players = ["Костя", "Витя", "Саша", "Даша", "Кирилл", "Маша", "Тима", "Вика"]
total_players = len(list_players)

middle_index = total_players // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print(first_team)
print(second_team)