


# Task 6

# Create two string variables bigger than the length 3.
# If the second string starts with the first string’s last three
# characters, print true. If not, print false.



print("Please enter a text name:")
str = input()

print("Please enter a text name:")
str1 = input()

last_three_chs_of_str = str[len(str)-3]
first_three_chs_of_str1 = str1[2]

is_first3_last3 = last_three_chs_of_str == first_three_chs_of_str1
print(is_first3_last3)







