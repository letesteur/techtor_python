


nums = [1,2,3,1,2,3,4,2,2,2]


# Remove all the number 2's from this list.
# First I can find count of 2's in the list 
# I can apply the remove method count times.
count = 0
for number in nums:
    if number == 2:
        count+=1
print(count)
# i need to apply the remove method count times
# i need to crete a loop that iterates count times

#How many times the loop will get executed?
#It will get executed count times
for i in range(count):
    nums.remove(2)
print(nums)



nums = [1,2,3,1,2,3,4,2,2,2]


# Remove all the number 2's from this list.

# I can create a copy of this list
newList = nums.copy()

for number in newList:
    if number == 2:
        nums.remove(2)
print(nums)