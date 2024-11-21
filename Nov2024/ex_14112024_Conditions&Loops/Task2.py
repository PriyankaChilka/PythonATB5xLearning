
"""
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is
equilateral (all sides are equal),
isosceles (exactly two sides are equal),
or scalene (no sides are equal).
 Use an if-else statement to classify the triangle.
"""
# User Inputs => 3 Sides of Triangle, type float
# Logic if elif else logic

side1 = float(input("Please enter first side of a triangle :"))
side2 = float(input("Please enter second side of a triangle :"))
side3 = float(input("Please enter third side of a triangle :"))

print("The sides of a triangle are :", side1,side2,side3)

#Logic

if(side1==side2 and side1==side3 and side2==side3):
    print ("It is an Equilateral triangle.")
elif (side1==side2 or side1==side3 or side2==side3):
    print ("It is an Isosceles triangle.")
else :
    print("It is a Scalene triangle")
