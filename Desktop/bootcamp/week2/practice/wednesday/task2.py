# Вы собираетесь на Иссык-Куль. Пока ваш чемодан пуст: suitcase = [ ]. Однако он
# может вместить всего 5 вещей.
# a. Положите 5 вещей в чемодан с помощью метода .append()
# b. Вы передумали, и решили убрать последнюю вещь. Вспомните, какой метод
# помогает удалить последний элемент.
# c. Вы решили положить в чемодан другую вещь, только в первое место (т.е. по
# индексу 0). Вспомните метод, который ставит элементы по индексу.

suitcase = []
for i in range (5):
    suitcase.append(i)
print(suitcase)
suitcase.pop()
print(suitcase)
suitcase.insert(0, 9)
print(suitcase)