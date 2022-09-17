

# User wants to deposit his money into his bank account
# he already has $200 in his account
# He has three different paychecks 400, 600 and 350
# he can only deposit all the money in the account
# After he deposit all the money in the account
# he bough a phone for $599, and headphone for $299
# Create a python program to calculate his final money in the account
# Use input function to get all the values

bank_acc = 200
print("Please enter first paycheck amount: ")
paycheck1 = int(input())

bank_acc +=paycheck1

print("Please enter second paycheck amount: ")
paycheck2 = int(input())

bank_acc +=paycheck2

print("Please enter third paycheck amount: ")
paycheck3 = int(input())

bank_acc +=paycheck3

print("Please enter the dollar amount of phone you want to buy: ")
phone = int(input())

bank_acc -= phone

print("Please enter the dollar amount of head phone you want to buy: ")
head_phone = int(input())

bank_acc -= head_phone
print(" His final money in the bank account is", bank_acc)
