
# Task 1
# Create a program that will add up the value of a number of
# quarters, dimes, nickels, and pennies. The number of each
# type of coin is input by the user. The total value is printed in
# dollars.
# Example:
# Quarters: 5
# Dimes: 4
# Nickels: 3
# Pennies: 2
# The total in dollars is $1.82



print("Please enter the count of each coin type:")
quarters = int(input("Quarters: "))
dimes = int(input("Dimes: "))
nickels = int(input("Nickels: "))
pennies = int(input("Pennies: "))
total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
print("The total value of change", total)

