for i in range(0, 10, 1): # 0 to 9
    if i == 6 or i == 5:
        print(i)
    else:
        pass # pass is a placeholder statement that does nothing
    # It's used when a statement is syntactically required but no action is needed.


# | i  | Condition | O/P
# | 0  | 0 == 6 -> False | O/P - Nothing will be printed
# | 1  | 1 == 6 -> False | O/P - Nothing will be printed
# | 2  | 2 == 6 -> False | O/P - Nothing will be printed
# | 3  | 3 == 6 -> False | O/P - Nothing will be printed
# | 4  | 4 == 6 -> False | O/P - Nothing will be printed
# | 5  | 5 == 5 -> True | O/P - 5
# | 6  | 6 == 5 -> True | O/P - 6
# | 7  | 7 == 6 -> False | O/P - Nothing will be printed
# | 8  | 8 == 6 -> False | O/P - Nothing will be printed
# | 9  | 9 == 6 -> False | O/P - Nothing will be printed
# | 10  | 10 == 6 -> For loop finished


for i in range(0, 10):  # 0 to 9, times -> 10
    print(i)
    if i == 5:
        break

# |i | Condition |  O/P
# |0 |  0 == 5 -> False |  O/P = 0
# |1 |  1 ==5 -> False |  O/P = 1
# |2 |  2 ==5 -> False |  O/P = 2
# |3 |  3 ==5 -> False |  O/P = 3
# |4 |  4 ==5 -> False |  O/P = 4
# |5 |  5 ==5 -> True |  O/P = BREAK out of For loop

for number in range(10):  # number - 0 to 9, times 10
    if number % 2 == 0:
        continue
    else:
        print(number)

# | i  | Condition | O/P
# | 0  | 0%2 == 0 -> True | continue - skip No O/P
# | 1  | 1%2 == 0 -> False | 1


# pass - can be used in the statement, fucntions, classes and objects.