"""
Checking for a Leap Year , 2024 → Yes

Leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400.
"""

#User input >Input

year = int(input("Please enter a year to check whether is a leap year or Not\n"))

if (year%4==0 and (year%100!=0 or year%400==0)):
    print(f"{year} is a leap year.")
else :
    print(f"{year} is Not a leap year.")

