

# Task 4
#Using input function ask user to enter a song name.
# 1. Print the first charachter of given song name.
# 2. Print the last charachter of given song name.
# 3. Print the length of the given song name.
# 4. Print the index number of "k" in this song name.
# 5. Print the charachter from an index number of 3.
# 6. Print the song name in upper case.
# 7. Print the song name in lower case.
# Example:
# Input: Mockingbird
# Output:
# M
# d
# 10
# 3
# k
# MOCKINGBIRD
# mockingbird



print("Enter a song name:")
song_name = input()

# 1. Print the first charachter of given song name.
first_char = song_name[:1]
print(first_char) 

# 2. Print the last charachter of given song name.
last_char = song_name[-1]
print(last_char)

# 3. Print the length of the given song name.
song_name_lenght = len(song_name)
print(song_name_lenght)

# 4. Print the index number of "k" in this song name.
index_of_k = song_name.index("k")
print(index_of_k)

# 5. Print the charachter from an index number of 3.
char_of_3index = song_name[3:4]
print(char_of_3index)

# 6. Print the song name in upper case.
upper_case = song_name.upper()
print(upper_case)

# 7. Print the song name in lower case.
lower_case = song_name.lower()
print(lower_case)
