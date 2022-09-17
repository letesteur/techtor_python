


# Using the input function asks the user to input the min and
# max number. Write a python code that will calculate the sum
# of numbers between the range of min and max and those that
# can only be divided by 3 and 11.
# (min and max numbers are included)
# Example:
# 0, 99 -> 33 + 66 + 99 = 198

print("enter a number")
num = int(input())

print("enter a number bigger than first one")
num2 = int(input())
sum =0
text = ""
for n in range(num,num2):
    if n % 11 ==0 and n % 3 ==0:
        text = text + str(n) +  " + "
        sum+=n

print(text.removesuffix(" + "),"=" , sum)

