# 5. Больше гостей: вы решили купить обеденный стол большего размера. Дополнительные
# места позволяют пригласить на обед еще трех гостей.
# • Начните с программы из упражнения 3 или 4. Добавьте в конец программы команду print, которая выводит сообщение о расширении списка гостей.
# • Добавьте вызов insert() для добавления одного гостя в начало списка.
# • Добавьте вызов insert() для добавления одного гостя в середину списка.
# • Добавьте вызов append() для добавления одного гостя в конец списка.
# • Выведите новый набор сообщений с приглашениями – по одному для каждого участника, входящего в список.

guest = ['Azat', 'Azamat', 'Asylbek']
print("Some friends will join us:")
guest.insert(0, 'Davran')
guest.insert(2, 'Kanybek')
guest.append('Erlan')
print(guest)
print("Let us have a lunch " + guest[0] + "")
print("Let us have a lunch " + guest[1] + "")
print("Let us have a lunch " + guest[2] + "")
print("Let us have a lunch " + guest[3] + "")
print("Let us have a lunch " + guest[4] + "")
print("Let us have a lunch " + guest[5] + "")