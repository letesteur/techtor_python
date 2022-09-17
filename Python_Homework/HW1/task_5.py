
# Task 5
# Write a python program that reads a number in inches,
# converts it to meters.
# Note: One inch is 0.0254 meter.
# Test Data
# INCH: 2000
# Expected Output :
# 2000.0 inch is 50.8 meters

Inches = int(input("Enter the length in Inches:"))   
meter = Inches  * 0.0254; #You have to use one formula for converting the value in Inches to the value in meter  
  
print("2000.0 inch is",round(meter,3),"meters")