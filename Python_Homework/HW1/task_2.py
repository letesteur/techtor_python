
# Task 2
# Write a program that will take a given amount of
# money and return the number of dollars in quarters,
# dimes, nickels, and pennies that make up that given
# amount
# Example 1:
# Please enter your balance:
# 2.36
# $2.36 will make 9 quarters 1 dime 0 nickels and 1
# pennies

dollar = float(input("Please enter your balance $: "))
dollar_amount = dollar * 100

quarter_value = 25
dime_value = 10
nickel_value = 5
penny_value = 1
            
result_quarter = dollar_amount // quarter_value 
print(result_quarter, "quarters")                           
remaining_exchange_quarter = dollar_amount % quarter_value

result_dime = remaining_exchange_quarter // dime_value
print(result_dime , "dimes")
remaining_exchange_dimes = remaining_exchange_quarter % dime_value

result_nickel = remaining_exchange_dimes // nickel_value
print(result_nickel, "nickels")
remaining_exchange_nickel = remaining_exchange_dimes % nickel_value

result_penny = remaining_exchange_nickel // penny_value
print(result_penny,"pennies")