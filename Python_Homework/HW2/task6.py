
# Task 6
# Write the program to get the string value from the specified position.
# First, ask the user to enter one String value. Then ask the user to the
# enter starting number and ending number. After that, print the value
# between the given starting and ending numbers. (Note: since the user
# does not know the python, the user starts counting from 1, and the
# ending number will be included)
# Example:
# Please enter the String value:
# Definition of Science
# Please enter the starting number:
# 2
# Please enter the ending number
# 5
# The output is:
# efin

print("Please enter a string")

str1 = input()

print("Please enter start number:")

num1 = int(input())

print("Please enter end number:")

num2 = int(input())

result = str1[(num1):num2]
print(result)






























