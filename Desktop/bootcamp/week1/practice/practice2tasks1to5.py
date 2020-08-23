# *************** Типы данных. Numbers ******************

# Числовой тип данных в Python предназначен для хранения числовых значений. Это неизменяемый тип данных, что означает, что изменение значения числового типа данных приведет к созданию нового объекта в памяти (и удалению старого)

# Числовые объекты создаются, когда вы присваиваете им значение. Например:

# num1 = 33
# num2 = 44


# Также вы можете удалять числовой объект при помощи ключевого слова del. Синтаксис команды del следующий:

# del num1 # удаляет переменную num1
# del num1, num2 # удаляет обе переменные num1 за num2 за раз


# В Python есть четыре вида числового типа данных:

#   * int (целое число)
#   * long (длинное целое число [может быть представлено в восьмеричной или шестнадцатеричной системе исчисления])
#   * float (число с плавающей точкой: -0.2, 0.0, 3.14159265 и т.д.)
#   * complex (комплексное число) 


# ******************* Целые числа (int) ****************

# Числа в Python 3 ничем не отличаются от обычных чисел. Они поддерживают набор самых обычных математических операций:

# x + y	Сложение
# x - y	Вычитание
# x * y	Умножение
# x / y	Деление
# x // y	Получение целой части от деления
# x % y	Остаток от деления
# -x	Смена знака числа
# abs(x)	Модуль числа
# divmod(x, y)	Пара (x // y, x % y)
# x ** y	Возведение в степень
# pow(x, y[, z])	xy по модулю (если модуль задан)

# Также нужно отметить, что целые числа в python 3, в отличие от многих других языков, поддерживают длинную арифметику (однако, это требует больше памяти).


# 255 + 34 #289
# 5 * 2 #10
# 20 / 3 #6.666666666666667
# 20 // 3 #6 
# 20 % 3 #2
# 3 ** 4 #81
# pow(3, 4) #81
# pow(3, 4, 27) #0
# 3 ** 150 #369988485035126972924700782451696644186473100389722973815184405301748249


# Битовые операции
# Над целыми числами также можно производить битовые операции

# x | y	Побитовое или
# x ^ y	Побитовое исключающее или
# x & y	Побитовое и
# x << n	Битовый сдвиг влево
# x >> y	Битовый сдвиг вправо
# ~x	Инверсия битов


# Системы счисления.

# Те, у кого в школе была информатика, знают, что числа могут быть представлены не только в десятичной системе счисления. К примеру, в компьютере используется двоичный код, и, к примеру, число 19 в двоичной системе счисления будет выглядеть как 10011. Также иногда нужно переводить числа из одной системы счисления в другую. Python для этого предоставляет несколько функций:

# int([object], [основание системы счисления]) - преобразование к целому числу в десятичной системе счисления. По умолчанию система счисления десятичная, но можно задать любое основание от 2 до 36 включительно.
# bin(x) - преобразование целого числа в двоичную строку.
# hex(х) - преобразование целого числа в шестнадцатеричную строку.
# oct(х) - преобразование целого числа в восьмеричную строку.

# a = int('19') # Переводим строку в число
# b = int('19.5')  # Строка не является целым числом
# c = int(19.5)  # Применённая к числу с плавающей точкой, отсекает дробную 
# print(a, c) #19 19
# bin(19) #'0b10011'
# oct(19) #'0o23'
# hex(19) #'0x13'

# 0b10011  # Так тоже можно записывать числовые константы (19)
# int('10011', 2) #19
# int('0b10011', 2) #19


# ************** Вещественные числа (float) **************

# Вещественные числа поддерживают те же операции, что и целые. Однако (из-за представления чисел в компьютере) вещественные числа неточны, и это может привести к ошибкам:

# 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 #0.9999999999999999


# Для высокой точности используют другие объекты (например Decimal и Fraction))
# Также вещественные числа не поддерживают длинную арифметику:

# a = 3 ** 1000
# a + 0.1
# # OverflowError: int too large to convert to float


# Примеры работы с числами:

# c = 150
# d = 12.9
# print(c + d) #162.9

# p = abs(d - c)  # Модуль числа
# print(p) # 137.1
# round(p)  # Округление (137)

# Дополнительные методы

# float.as_integer_ratio() - пара целых чисел, чьё отношение равно этому числу.

# float.is_integer() - является ли значение целым числом.

# float.hex() - переводит float в hex (шестнадцатеричную систему счисления).

# classmethod float.fromhex(s) - float из шестнадцатеричной строки.

# (10.5).hex() #'0x1.5000000000000p+3'
# float.fromhex('0x1.5000000000000p+3') #10.5

# Помимо стандартных выражений для работы с числами (а в Python их не так уж и много), в составе Python есть несколько полезных модулей.

# Модуль math предоставляет более сложные математические функции.

# import math
# math.pi  #3.141592653589793
# math.sqrt(85) #9.219544457292887

# Модуль random реализует генератор случайных чисел и функции случайного выбора.

# import random
# random.random() #0.15651968855132303

# *********************** Комплексные числа (complex) **********************

# В Python встроены также и комплексные числа:

# x = complex(1, 2)
# print(x) #(1+2j)

# y = complex(3, 4) 
# print(y) #(3+4j)

# z = x + y
# print(x) #(1+2j)

# print(z) #(4+6j)

# z = x * y
# print(z) #(-5+10j)

# z = x / y
# print(z) #(0.44+0.08j)

# print(x.conjugate())  # Сопряжённое число (1-2j)

# print(x.imag)  # Мнимая часть (2.0)

# print(x.real)  # Действительная часть (1.0)

# print(x > y)  # Комплексные числа нельзя сравнить
# # TypeError: unorderable types: complex() > complex()

# print(x == y)  # Но можно проверить на равенство (False)

# abs(3 + 4j)  # Модуль комплексного числа (5.0)

# pow(3 + 4j, 2)  # Возведение в степень (-7+24j)

# Также для работы с комплексными числами используется также модуль cmath.




# # Task 1.
# # """
# # Write a function is_even that takes
# # in a number and returns True if it is even,
# # otherwise False.
# # BONUS CHALLENGE:
# # Write the function solution in 1 line
# # of code without using if statements.
# # """
# #Make sure to un-comment the function line below when you are done.
# #Remember to name your function is_even()
# def is_even(number):
#   if number % 2 == 0
#   return True
# else:
#   return False

# #DO NOT_to_choice remove lines below here,
# #this is designed to test your code.
# def test_is_even():
#   assert is_even(2) == True
#   assert is_even(3) == False
#   assert is_even(8) == True
#   assert is_even(100) == True
#   assert is_even(101) == False
#   print("YOUR CODE IS CORRECT!")
# #test your code by un-commenting the line(s) below
# # test_is_even()




# Task 2.
# """
# Write a function square_number that
# takes in a number and squares it.
# """
# #Make sure to un-comment the square_test() line below
# #when you are done.
# #     WRITE YOUR CODE HERE...
# def square_number(2):
#   return number ** 2

# print (square_number(2))

# # #DO NOT remove lines below here,
# # # #this is designed to test your code.
# def test_square_number():
# assert square_number(2) == 4
# assert square_number(8) == 64
#   assert square_number(10) == 100
#   print("YOUR CODE IS CORRECT!")
# # #test your code by un-commenting the line(s) below
# test_square_number()




# Task 3
# """
# Write a function bigger_guy that takes in
# two numbers and returns the bigger one.
# MAKE SURE to use RETURN and not PRINT in your function.
# Ex: bigger_guy(10, 20) # --> 20
# """
#Make sure to un-comment the function line below when you are done.
#Remember to name your function correctly.
#     WRITE YOUR CODE HERE...
# def bigger_guy(num1, num2):
#   if num1 > num2: 
#   return num1
# else:
#   return num2

# #DO NOT remove lines below here,
# #this is designed to test your code.
# def test_bigger_guy():
#   assert bigger_guy(1, 2) == 2
#   assert bigger_guy(10, 20) == 20
#   assert bigger_guy(20, 10) == 20
#   assert bigger_guy(10, 10) == 10
#   assert bigger_guy(2, 1) == 2
#   assert bigger_guy('a', 'b') == 'b' # 'b' is greater than 'a'
#   print("YOUR CODE IS CORRECT!")
# #test your code by un-commenting the line(s) below
# #test_bigger_guy()




# Task 4
# """
# Write a function biggest_guy that takes in
# three numbers as input and returns the biggest one.
# MAKE SURE to use RETURN and not PRINT in your function.
# Ex: biggest_guy(10, 30, 20) # --> 30
# BONUS CHALLENGE: Write a 1 line solution (Medium Difficulty)
# HINT: Maybe use the bigger_guy function...
# """
#Make sure to un-comment the function line below when you are done.
#Remember to name your function correctly.
# def bigger_guy():
#    WRITE YOUR CODE HERE...
def biggest_guy(num1, num2, num3):
  if num1 > num2:
    bigger_guy = num1
  else:
    bigger_guy = num2
  if bigger_guy >num3:
    biggest_guy = bigger_guy
  else:
    biggest_guy = num3
  return biggest_guy
#DO NOT remove lines below here,
#this is designed to test your code.
def test_biggest_guy():
    assert biggest_guy(1, 3, 2) == 3
    assert biggest_guy(30, 10, 20) == 30
    assert biggest_guy(20, 10, 30) == 30
    assert biggest_guy(2, 1, 9) == 9
    assert biggest_guy('a', 'a', 'b') == 'b' # 'b' is greater than 'a'
    print("Correct buddy!!!")
#test your code by un-commenting the line(s) below
test_biggest_guy()




# Task 5
# """
# Backstory: Usain Bolt, you, and Aybek
# had a race. Surprisingly, Usain bolt won.
# You came in 2nd and Aybek came in 3rd :(.
# Can you think of a way to write a function
# that given a person's name, returns his/her place?
# ALSO
# Can you think of a way to write a function
# that given a place, returns his/her name?
# WRITE 2 FUNCTIONS
# One that converts choice to number
# and
# One that converts number to choice.
# """
#Make sure to un-comment the code test line
#all the way below when you are done.
#Remember to name your function correctly.
#   WRITE YOUR CODE HERE...
def choice_to_number(choice):
# """Convert choice to number."""
# If choice is Usain you should get back 1.
if choice == "Usain":
  return 1
elif choice == "me":
  return 2
elif choice == "Aybek";
  return 3

def number_to_choice(number):
# """Convert number to choice."""
# if number is 1 then return usain bolt.
#DO NOT remove lines below here,
#this is designed to test your code.
# def test_choice_to_number():
#   assert choice_to_number('Usain') == 1
#   assert choice_to_number('Me') == 2
#   assert choice_to_number('Aybek') == 3
# def test_number_to_choice():
#   assert number_to_choice(1) == 'Usain'
#   assert number_to_choice(2) == 'Me'
#   assert number_to_choice(3) == 'Aybek'
# def test_all():
  # try:
# test_choice_to_number()
#     test_number_to_choice()
#   except AssertionError:
#     print(‘WRONG’)
#   else:
#     print(‘SUCCESS’)
#test your code by un-commenting the line(s) below
#test_all()
 
