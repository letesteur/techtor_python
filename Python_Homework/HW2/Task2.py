


# Ask user to enter any string value using input function.
# Then, remove all the spaces (" ") from the given string.
# After removing the spaces from the string,
# if the string's length is odd print True, otherwise print False.

# Example:
# Input : I love coding
# Output: True
# Input : one two
# Output: False



print("Please enter a string:")
str = input()
removed_spaces = str.replace(" ", "")
print(removed_spaces)

len_of_str = len(removed_spaces)
if len_of_str % 2 == 0:
    print("False")
else:
    print("True")