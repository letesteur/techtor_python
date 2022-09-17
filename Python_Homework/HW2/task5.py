
# Task 5
# Using an input function enter three different ingredients for the product
# on the same line. Then ask the user to enter any int number. Change the
# first letter of the ingredients starting from the entered number.
# (Ingredients should start with different letters. Please read the example
# carefully ) Example 1:
# Please enter three ingredients with spaces:
# Milk Peanuts Butter
# Please enter the int number:
# 5
# The output is:
# 5ilk 6eanuts 7utter

print("Please enter three ingredients with spaces:")

item_name = input().split()
print(item_name)
item1 = item_name[0]
item2 = item_name[1]
item3 = item_name[2]


print("Please enter count for each item:")

item_count = input().split()
print(item_count)
count1 = item_count[0]
count2 = item_count[1]
count3 = item_count[2]

concat1 = str(count1)+item1[1:]
concat2 = str(count2)+item2[1:]
concat3 = str(count3)+item3[1:]
print(concat1,concat2,concat3)






