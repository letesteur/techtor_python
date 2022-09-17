



# Reverse a given String and print it, if they have space in the
# beginning and at the end then remove it. Without using
# slicing [ : :-1]. Try doing with for loop or while loop.
# Example: " Job" -> "boJ"
# * " Happy " -> "yppaH"
# * "Sun " -> "nuS"
# * " Dream Job!" -> "!boJ maerD"


print("Please enter a string with space at the beging of the string:")
str1 = str(input())
remove_space = str1.strip()
reverse_str = ""
for char in remove_space:
    reverse_str = char + reverse_str

print(reverse_str)




