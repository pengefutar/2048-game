""" Welcome to Eszti and Tomi's 2048 game! =) """


import os
import random
from copy import deepcopy

""" The starter table """
j = [[" ", " ", " ", " "],
     [" ", " ", " ", " "],
     [" ", " ", " ", " "],
     [" ", " ", " ", " "]]

"""
Tables for testing winning and losing.
Win by moving left at the first one, and
lose by moving up or down at the second one.

j = [["1024", "1024", " ", " "],
     [" ", " ", " ", " "],
     [" ", " ", " ", " "],
     [" ", " ", " ", " "]]

j = [["4", "8", "16", "32"],
     ["64", "128", "256", "8"],
     ["8", "4", "32", "4"],
     ["8", "32", "4", "32"]]
"""

points = 0

k = [[" ", " ", " ", " "],
     [" ", " ", " ", " "],
     [" ", " ", " ", " "],
     [" ", " ", " ", " "]]


def madeby():
    """ Credits, instructions, and points """

    print("""\033[0;34m
      M    M    AA    DDDDD    EEEEEE        BBBBB  YY    YY
      MM  MM   A  A   D   DD   EE            BB   B  YY  YY
      M MM M  AAAAAA  D    DD  EEEE          BBBBB     YY
      M    M  A    A  D   DD   EE            BB   B    YY
      M    M  A    A  DDDDD    EEEEEE        BBBBB     YY


      EEEEEE  SSSSSS  ZZZZZZ  TTTTTT  II         AA    N    N  DDDDD         TTTTTT   OOOO   M    M   II
      EE      SS         ZZ     TT    II        A  A   NN   N  D   DD          TT    OO  OO  MM  MM   II
      EEEE    SSSSSS    ZZ      TT    II       AAAAAA  N N  N  D    DD         TT    OO  OO  M MM M   II
      EE          SS   ZZ       TT    II       A    A  N  N N  D   DD          TT    OO  OO  M    M   II
      EEEEEE  SSSSSS  ZZZZZZ    TT    II       A    A  N   NN  DDDDD           TT     OOO0   M    M   II\x1b[0;0m


      \033[0;31mUse WASD to shift
      Press N to start a new game
      Press G to give up\x1b[0;0m
      
      \033[0;33mPoints:\x1b[0;0m \033[1;33m{points}\x1b[0;0m
      """.format(points=points))


def colors():
    """ K has the same values as J, except the K is colored. 
    If we colored the original list, the formatted strings couldn't be 
    turned into integers when the same numbers next to each other are added together.
    This function is checking the present state of J, and modifies K according to that.
    Also, the width of the values is always 4 and they are right-aligned.
    """

    g = 0
    while g <= 3:
        f = 3
        while f >= 0:

            if j[g][f] == " ":
                k[g][f] = "    "

            if j[g][f] == "2":
                k[g][f] = "\033[1;33m{num:>{width}}\x1b[0;0m".format(
                    num="2", width=4)
            if j[g][f] == "4":
                k[g][f] = "\033[1;38m{num:>{width}}\x1b[0;0m".format(
                    num="4", width=4)
            if j[g][f] == "8":
                k[g][f] = "\033[1;36m{num:>{width}}\x1b[0;0m".format(
                    num="8", width=4)
            if j[g][f] == "16":
                k[g][f] = "\033[1;35m{num:>{width}}\x1b[0;0m".format(
                    num="16", width=4)
            if j[g][f] == "32":
                k[g][f] = "\033[1;32m{num:>{width}}\x1b[0;0m".format(
                    num="32", width=4)
            if j[g][f] == "64":
                k[g][f] = "\033[1;31m{num:>{width}}\x1b[0;0m".format(
                    num="64", width=4)
            if j[g][f] == "128":
                k[g][f] = "\033[1;38m{num:>{width}}\x1b[0;0m".format(
                    num="128", width=4)
            if j[g][f] == "256":
                k[g][f] = "\033[1;36m{num:>{width}}\x1b[0;0m".format(
                    num="256", width=4)
            if j[g][f] == "512":
                k[g][f] = "\033[1;35m{num:>{width}}\x1b[0;0m".format(
                    num="512", width=4)
            if j[g][f] == "1024":
                k[g][f] = "\033[1;32m{num:>{width}}\x1b[0;0m".format(
                    num="1024", width=4)
            if j[g][f] == "2048":
                k[g][f] = "\033[1;31m{num:>{width}}\x1b[0;0m".format(
                    num="2048", width=4)
            f -= 1
        g += 1


def print_table():
    """The terminal gets cleared. The credits, instructions, and points show up, 
    the colored, right-aligned version of the list gets created in K, 
    and the K is printed in a table format. 
    """

    os.system('cls' if os.name == 'nt' else 'clear')
    madeby()
    colors()
    row_length = 29
    line = "-" * row_length
    print("      ", *line, sep='')
    for n in k:
        print("      |      |      |      |      |")
        print("      |", "{text:>{width}}".format(
            text=n[0], width=4),
            "|", "{text:>{width}}".format(
            text=n[1], width=4),
            "|", "{text:>{width}}".format(
            text=n[2], width=4),
            "|", "{text:>{width}}".format(
            text=n[3], width=4),  "|")
        print("      ", *line, sep='')
    print()


def randomize():
    """Twos get created in one of the empty spaces.
    We collect the coordinates of the empty spaces in a list of tuples,
    and the function randomly chooses one between them and places a two there.
    """

    list_of_empty = []

    g = 0
    while g <= 3:
        f = 3
        while f >= 0:
            if j[g][f] == " ":
                list_of_empty.append((g, f))
            f -= 1
        g += 1

    if list_of_empty != []:
        rand1 = (random.randint(0, len(list_of_empty) - 1))
        j[list_of_empty[rand1][0]][list_of_empty[rand1][1]] = "2"
    else:
        pass


def shifting_r():
    """Shifting the numbers right by changing positions with the empty places"""

    z = 0

    while z < 3:
        x = 0
        for x in range(4):
            y = 3
            while y > 0:
                if j[x][y] == " ":
                    j[x][y] = j[x][y - 1]
                    j[x][y - 1] = " "
                y -= 1
            x += 1
        z += 1


def adding_r():
    """Adding the same numbers next to each other to right.
    Every time a sum is done, the user gets as many points for it
    as the value of the added numer is.
    """

    global points

    x = 0
    for x in range(4):
        y = 3
        while y > 0:
            if j[x][y] != " " and j[x][y] == j[x][y - 1]:
                j[x][y] = int(j[x][y - 1]) + int(j[x][y])
                points = points + j[x][y]
                j[x][y] = str(j[x][y])
                j[x][y - 1] = " "
            y -= 1
        x += 1


def shifting_l():
    """Shifting left"""

    z = 0

    while z < 3:
        x = 0
        for x in range(4):
            y = 0
            while y < 3:
                if j[x][y] == " ":
                    j[x][y] = j[x][y + 1]
                    j[x][y + 1] = " "
                y += 1
            x += 1
        z += 1


def adding_l():
    """Adding left"""

    global points

    x = 0
    for x in range(4):
        y = 0
        while y < 3:
            if j[x][y] != " " and j[x][y] == j[x][y + 1]:
                j[x][y] = int(j[x][y + 1]) + int(j[x][y])
                points = points + j[x][y]
                j[x][y] = str(j[x][y])
                j[x][y + 1] = " "

            y += 1
        x += 1


def shifting_d():
    """Shifting down"""

    z = 0

    while z < 3:
        y = 0
        for y in range(4):
            x = 3
            while x > 0:
                if j[x][y] == " ":
                    j[x][y] = j[x - 1][y]
                    j[x - 1][y] = " "
                x -= 1
            y += 1
        z += 1


def adding_d():
    """Adding down"""

    global points

    y = 0
    for y in range(4):
        x = 3
        while x > 0:
            if j[x][y] != " " and j[x][y] == j[x - 1][y]:
                j[x][y] = int(j[x - 1][y]) + int(j[x][y])
                points = points + j[x][y]
                j[x][y] = str(j[x][y])
                j[x - 1][y] = " "
            x -= 1
        y += 1


def shifting_u():
    """Shifting up"""

    z = 0

    while z < 3:
        y = 0
        for y in range(4):
            x = 0
            while x < 3:
                if j[x][y] == " ":
                    j[x][y] = j[x + 1][y]
                    j[x + 1][y] = " "
                x += 1
            y += 1
        z += 1


def adding_u():
    """Adding up"""

    global points

    y = 0
    for y in range(4):
        x = 0
        while x < 3:
            if j[x][y] != " " and j[x][y] == j[x + 1][y]:
                j[x][y] = int(j[x + 1][y]) + int(j[x][y])
                points = points + j[x][y]
                j[x][y] = str(j[x][y])
                j[x + 1][y] = " "
            x += 1
        y += 1


def right():
    """This function gets called when the user chooses the right direction. 
    The numbers get shifted, added, and shifted again to the right, 
    and if there was a change in the list (it gets checked with the deepcopy of j in the r), 
    a two gets generated in a random empty place.
    """

    r = deepcopy(j)
    shifting_r()
    adding_r()
    shifting_r()
    if r != j:
        randomize()


def left():
    """Same as previous, but the direction is the left"""

    r = deepcopy(j)
    shifting_l()
    adding_l()
    shifting_l()
    if r != j:
        randomize()


def down():
    """Same as previous, but the direction is down"""

    r = deepcopy(j)
    shifting_d()
    adding_d()
    shifting_d()
    if r != j:
        randomize()


def up():
    """Same as previous, but the direction is up"""

    r = deepcopy(j)
    shifting_u()
    adding_u()
    shifting_u()
    if r != j:
        randomize()


def give_up():
    """Message when the user gives up"""

    print()
    print("\033[1;32m      Byebye! We hope you enjoyed the game! :)\x1b[0;0m")
    print()
    exit()


def new_game():
    """Generating a new empty table when the user starts a new game"""

    global j
    global points
    points = 0
    j = [[" ", " ", " ", " "], [" ", " ", " ", " "],
         [" ", " ", " ", " "], [" ", " ", " ", " "]]
    randomize()
    randomize()


def loser():
    """If there is no empty place in the table, the function checks
    if there is any other move left. An empty list is generated,
    and if the program finds the same numbers next to each other, 
    it adds something to the list. If the list stays empty
    (no same numbers being next to each other), and there are no
    empty places left either, the game is lost. A message is printed,
    and the game exits.
    """

    global j
    if (" " not in j[0] and
        " " not in j[1] and
        " " not in j[2] and
            " " not in j[3]):
        same = []

        mm = 3
        while mm > 0:
            m = 3
            while m > 0:
                if j[0][m] == j[0][m - 1]:
                    same.append(1)
                if j[1][m] == j[1][m - 1]:
                    same.append(1)
                if j[2][m] == j[2][m - 1]:
                    same.append(1)
                if j[3][m] == j[3][m - 1]:
                    same.append(1)
                m -= 1

            m = 3
            while m >= 0:
                if j[0][m] == j[1][m]:
                    same.append(1)
                if j[1][m] == j[2][m]:
                    same.append(1)
                if j[2][m] == j[3][m]:
                    same.append(1)
                m -= 1
            mm -= 1
            lose = False

        if same == []:
            lose = True

        if lose == True:
            print_table()

            print()
            print("\033[1;31m      YOU LOSE, BITCH\x1b[0;0m")
            print()
            exit()


def winner():
    """If the function finds any 2048 in the table, the user wins.
    A message is printed, and the game exits.
    """

    global j
    if ("2048" in j[0] or
        "2048" in j[1] or
        "2048" in j[2] or
            "2048" in j[3]):
        print_table()
        print()
        print("\033[1;36m      CONGRATULATIONS! YOU WON!\x1b[0;0m")
        print("\033[1;36m      YOU'RE AWESOME!! :D\x1b[0;0m")
        print()
        exit()


def user_input():
    """The function executes the choice the user makes
    (left, right, up, down, new game, or give up)."""

    global j
    global points
    move = input("      ")

    if (move == "w" or move == "W"):
        up()

    if (move == "a" or move == "A"):
        left()

    if (move == "s" or move == "S"):
        down()

    if (move == "d" or move == "D"):
        right()

    if (move == "n" or move == "N"):
        new_game()

    if (move == "g" or move == "G"):
        give_up()


"""The main function generates two 2s to the empty table, and the game starts.
The table gets updated according to the state of the game, the move of the user 
is executed, and the conditions for both losing and winning is checked continuously.
"""

randomize()
randomize()

while True:

    print_table()
    user_input()
    loser()
    winner()
