

# Using the input function ask the user to enter one string value and
# print only unique letters combined as String also without any space in
# the beginning and at the end.
# Example -1 :
# Given Value: "i am happy"
# Output: i am hpy
# Example-2:
# Given Value: " contribute"
# Output: contribue
# Example-3:
# Given Value: " i want cup of coffee "
# Output: i want cup of e

print("Enter a sentence:")
word = str(input())
remove_space = word.rstrip
unique_letters = ""

for letters in word:
    if letters not in unique_letters:
        unique_letters += letters.lower()

print("The list of unique characters is:{}".format(unique_letters))

