# Создайте лист из чисел и определите количество четных и не четных.
a = input()
a = int(a)

even = 0
odd = 0

while a > 0:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    a = a // 10

print("Even: %d, odd: %d" % (even, odd))