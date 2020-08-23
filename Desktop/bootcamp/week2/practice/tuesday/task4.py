# Исходный список содержит положительные и отрицательные числа. Требуется положительные
# поместить в один список, а отрицательные - в другой.


def divide(array):
    positive = []
    negative = []
    for i in array:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
    return positive, negative
 
 
arr = [1, 2, 3, 4, 5, 6, 11, -1, -2, -3, -7, -20, -22]
pos, neg = divide(arr)
print(pos)
print(neg)