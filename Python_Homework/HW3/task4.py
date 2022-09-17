




# Ask the user to enter one in number between 1 to 10 then, Write the
# program to print the string in the following format:
# Search to see what happens when you multiply the string with
# numbers and use it for solving this question.
# Example:
# Input: 6
# Output:
# 666666
# 55555
# 4444
# 333
# 22
# 1



num = int(input("Enter a number between 10 to 1: "))
for l in range(num,0,-1):
    for ll in range(1,l+1):
        print(l,end="")
    print()
