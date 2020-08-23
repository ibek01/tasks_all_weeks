# Task 1.
# """
# Write a function is_even that takes
# in a number and returns True if it is even,
# otherwise False.
# BONUS CHALLENGE:
# Write the function solution in 1 line
# of code without using if statements.
# """
#Make sure to un-comment the function line below when you are done.
#Remember to name your function is_even()
def is_even(number):
    if (number % 2 == 0):
        return True
    return False

# #DO NOT_to_choice remove lines below here,
# #this is designed to test your code.
def test_is_even():
   assert is_even(2) == True
   assert is_even(3) == False
   assert is_even(8) == True
   assert is_even(100) == True
   assert is_even(101) == False
   print("YOUR CODE IS CORRECT!")
# #test your code by un-commenting the line(s) below
test_is_even()
