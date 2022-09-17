

# s = " Python is easy to learn "
# # From the given string above remove all the spaces and 
# # print the string

# print(s.replace(" ",""))

# # Let's replace word Python with Java 
# s = s.replace("Python","java") 
# # since replace method is 
# # case sensitive we have to use exact cases to replace

# print(s)

print("Enter a text with x'es")
str = input()

first_ch = str[0]
last_ch = str[-1]
middle_str = str[1:-1]
middle_str = middle_str.replace("x","")
print(first_ch+middle_str+last_ch)

