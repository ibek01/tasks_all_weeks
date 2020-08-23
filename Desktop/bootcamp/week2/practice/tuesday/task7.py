# Дан список чисел. Выведите все элементы списка, которые больше предыдущего
# элемента.(input:1, 5, 2, 4, 3 output: 5, 4)

a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])