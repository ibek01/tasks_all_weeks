# Дан список целых чисел. Заменить отрицательные на -1, положительные - на число 1, ноль
# оставить без изменений.

list1 = [22, -111, 4, 7, 0, 5, -88, 0, -1, 5]
listnew = []
for item in list1:
    if item > 0:
        listnew.append(1)
    elif item < 0:
        listnew.append(-1)
    else:
        listnew.append(0)

print(list1)
print(listnew)