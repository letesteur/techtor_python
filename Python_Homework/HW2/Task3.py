
# Task 3
# Using the input function ask the user to enter one sentence with three
# words and print the index number of each word's last character and then
# print the sum of each index number that you found.
# For Example:
# Input:
# "Importance of Human" --> it can be any three-word sentence.
# Output:
# 9 --> index number of 'e'
# 12 --> index number of 'f'
# 18 --> index number




from operator import index
from posixpath import split


print("Please enter a string:")

str = input()

index_find1 = str.rfind("e")
print("Index of 'e'", + index_find1)
index_find2 = str.rfind("f")
print("index of 'f'", +index_find2)
index_find3 = str.rfind("n")
print("index of 'n'", +index_find3)
print("Sum of each index is", index_find1+index_find2+index_find3)
