

## every math operation between float and int data type will result in float data type

from __future__ import division


floatNum = 3.0
intNum = 5
print("Type of floatNum is", type(float))
print("Type of intNum is", type(intNum))
addition = floatNum + intNum
print("Addition of float and int is", type(addition))

substraction = intNum - floatNum
print("Subsatraction between int and float is", type(substraction))

multiplication = floatNum * intNum
print("Multiplication between int data type and float is", type(multiplication))

division = floatNum / intNum
print("Division between float and int data type is", type(division))

remainder = floatNum % intNum
print("Remainder between float and int data type is", type(remainder))

remainder2 = intNum % floatNum
print("Remainder between float and int data type is", type(remainder2))

# There is only one way to get int wich is using //
int_division = floatNum // intNum
print("Integer symbol division result between float and integer is", type(int_division))

square_of_float = floatNum * floatNum
print(type(square_of_float))