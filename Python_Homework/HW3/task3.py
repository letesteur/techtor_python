


# Ask the user to enter one number between 1 to 10 then, Write the
# program to print the string in the following format:
# Search to see what happens when you multiply the string with
# numbers and use it for solving this question.
# Example:
# Input: 5
# Output:
# 1
# 22
# 333
# 4444
# 55555

num = int(input("Enter a number between 1 to 10:"))
for l in range(1, num+1):
    for ll in range(1, l+1):
        print(l,end="")
    print("")