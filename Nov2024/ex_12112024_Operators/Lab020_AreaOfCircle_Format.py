# Write a Python program to calculate the
# area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)

#Logic Building formula

# ||Step1||
#Figure out inputs and outputs
#input -> r -> datatype ->float
#pi=3.14
#power -> pow or **
#output -> float - area, print area

# ||Step2||
#rough logic = area = 3.14* pow(r,2)

# ||Step3||
radius= float(input("Enter radius of Circle\n"))
print (radius)
import math
area = (math.pi)*(radius**2)
print("Area of Circle is ",area)
print(f"Area of Circle is {area:.2f}")
