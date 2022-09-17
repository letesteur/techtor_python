
from re import T


bool1 = True
bool2 = False
bool3 = True

print(not bool3) # False
print(not bool2) # True

print(bool2 and bool1) # Since and condition requires bot side to be true for returning true this line will print false

print(bool2 or bool1) # If one of conditions is True, or will return True

print(bool2 or not bool1) # It will return false beacuse not operator will make the bool1 false so False or False will result in false

print(not bool2 and bool1) # It will return True because not operator will 
# make the bool2's value True so True and True will result in True

