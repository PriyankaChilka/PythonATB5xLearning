for i in range(0, 10):  # 0 to 9, times -> 10
    if i == 5:
        print("Five")
    else:
        print(i)

# |i | Condition |  O/P
# |0 |  0 == 5 -> False |  O/P = 0
# |1 |  1 ==5 -> False |  O/P = 1
# |2 |  2 ==5 -> False |  O/P = 2
# |3 |  3 ==5 -> False |  O/P = 3
# |4 |  4 ==5 -> False |  O/P = 4
# |5 |  5 ==5 -> True |  O/P = FIVE
# |6 |  6 ==5 -> False |  O/P = 6
# |9 |  9 ==5 -> False |  O/P = 9
# |10 |  10 ==5 -> False |  For loop finished - O/P = Exit


for i in range(0, 10, 1):
    if i == 6:
        print(i)
    else:
        print("No O/P")
        
# | i  | Condition | O/P
# | 0  | 0 == 6 -> False | O/P -> No O/P
# | 1  | 1 == 6 -> False | O/P -> No O/P
# | 2  | 2 == 6 -> False | O/P -> No O/P
# | 3  | 3 == 6 -> False | O/P -> No O/P
# | 4  | 4 == 6 -> False | O/P -> No O/P
# | 5  | 5 == 6 -> False | O/P -> No O/P
# | 6  | 5 == 6 -> True | O/P -> 6
# | 7  | 7 == 6 -> False | O/P -> No O/P
# | 8  | 8 == 6 -> False | O/P -> No O/P
# | 9  | 9 == 6 -> False | O/P -> No O/P