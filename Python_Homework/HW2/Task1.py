
# Task 1
# Please use method chaining for the following Strings. Methods are
# provided next to the String.
# String “ Snicker " —> strip, upper, remove prefix and slice the string with
# any number of your choice
# String “Cookie” —> lower, replace ‘o’ with ‘u’, remove suffix e,
# starts with ‘C’



str1 = "Snicker"
print(str1.strip("S"))
print(str1.upper())
#print(str1.removeprefix()) my Python doesn't recognize removeprefix and removesuffix functions
print(str1[5:-1])


str2 = "Cookie"
print(str2.lower(),(str2.replace("o", "u")),str2.startswith("C"), (str2.endswith("K")))





