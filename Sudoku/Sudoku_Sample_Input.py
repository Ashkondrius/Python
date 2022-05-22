# This is a simple Sudoku game on a 9x9 board that checks the conditions listed below:

# 1) Each row of the board must contain all digits from 1 to 9 (the order doesn't matter);
# 2) Each column of the board must contain all digits from 1 to 9 (again, the order doesn't matter);
# 3) Each of the nine 3x3 "tiles" (or "sub-squares") of the table must contain all digits from 1 to 9.

import sys

# We will use an empty dictionary to store each row input.

def begin():

    board = {"row1": (),
             "row2": (),
             "row3": (),
             "row4": (),
             "row5": (),
             "row6": (),
             "row7": (),
             "row8": (),
             "row9": ()
             }

    i = 1
    for key in board.keys():
        print("Please enter row nr", i, ":")
        board[key] = input()

        if not board[key].isdecimal():
            print("Your sample must be a string of numbers only. Please try again.")
            begin()
        if len(board[key]) != 9:
            print("The string must contain exactly 9 digits. Please try again.")
            begin()
        i += 1

    a = condition1(board)
    b = condition2(0, board)
    c = condition3(3, 0, board)

# If all 3 conditions mentioned above are fulfilled, the Sudoku sample is valid.

    print("Your board looks like this:")
    for values in board.values():
        print(values)
    print()

    if a == True and b == True and c == True:
        outcome = input("Sudoku is valid. Do you wish to continue? (y|n) ")
        outcome = outcome.upper()
        if outcome == "N":
            print("You have closed the game.")
            sys.exit()
        elif outcome == "Y":
            begin()
        else:
            sys.exit()
    else:
        outcome = input("Sudoku is not valid. Do you wish to continue? (y|n) ")
        outcome = outcome.upper()
        if outcome == "N":
            print("You have closed the game.")
            sys.exit()
        elif outcome == "Y":
            begin()
        else:
            print("You have closed the game.")
            sys.exit()

# We will compare each row with a string to determine if the sample is valid.

def condition1(board):

    for values in board.values():
        x = "123456789"

        for elem in values:
            if elem in x:
                x = x.replace(elem, "")
                continue

        if x != "":
            return False
    else:
        return True

# We will compare each column with a string to determine if the sample is valid.

def condition2(elem2, board):

    y = "123456789"
    x = "".join(values[elem2] for values in board.values())

    for elem in y:
        if elem in x:
            y = y.replace(elem, "")

    if y != "":
        return False
    elif elem2 < 8:
        return condition2(elem2 + 1, board)
    else:
        return True

# We will compare each sub-square with a string to determine if the sample is valid.

def condition3(elem3, a, board):

    z = "123456789"
    x = "".join(values[elem3 - 3:elem3] for values in board.values())

    for i in range(len(x)):
        if x[i] in z:
            z = z.replace(x[i], "")
        if (i + 1) % 9 == 0 and i > 0 and z != "":
            return False
        if (i + 1) % 9 == 0 and i > 0 and z == "":
            z = "123456789"

    if elem3 < 9:
        return condition3(elem3 + 3, a + 9, board)
    else:
        return True

begin()