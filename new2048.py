import os
import random


j = [[" ", " ", " ", " "], [" ", " ", " ", " "],
     [" ", " ", " ", " "], [" ", " ", " ", " "]]

k = [[" ", " ", " ", " "], [" ", " ", " ", " "],
     [" ", " ", " ", " "], [" ", " ", " ", " "]]


def madeby():

    print("""
      M    M    AA    DDDDD    EEEEEE        BBBBB  YY    YY
      MM  MM   A  A   D   DD   EE            BB   B  YY  YY
      M MM M  AAAAAA  D    DD  EEEE          BBBBB     YY
      M    M  A    A  D   DD   EE            BB   B    YY
      M    M  A    A  DDDDD    EEEEEE        BBBBB     YY


      \033[0;35mEEEEEE  SSSSSS  ZZZZZZ  TTTTTT  II\x1b[0;0m         AA    N    N  DDDDD     \033[0;34m    TTTTTT   OOOO   M    M   II\x1b[0;0m
      \033[0;35mEE      SS         ZZ     TT    II\x1b[0;0m        A  A   NN   N  D   DD    \033[0;34m      TT    OO  OO  MM  MM   II\x1b[0;0m
      \033[0;35mEEEE    SSSSSS    ZZ      TT    II\x1b[0;0m       AAAAAA  N N  N  D    DD   \033[0;34m      TT    OO  OO  M MM M   II\x1b[0;0m
      \033[0;35mEE          SS   ZZ       TT    II\x1b[0;0m       A    A  N  N N  D   DD    \033[0;34m      TT    OO  OO  M    M   II\x1b[0;0m
      \033[0;35mEEEEEE  SSSSSS  ZZZZZZ    TT    II\x1b[0;0m       A    A  N   NN  DDDDD     \033[0;34m      TT     OOO0   M    M   II\x1b[0;0m


      \033[0;31mUse WASD to shift
      Press N to start a new game
      Press G to give up\x1b[0;0m

      """)


def colors():

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

    list_of_zeros = []

    g = 0
    while g <= 3:
        f = 3
        while f >= 0:
            if j[g][f] == " ":
                list_of_zeros.append((g, f))
            f -= 1
        g += 1

    if list_of_zeros != []:
        rand1 = (random.randint(0, len(list_of_zeros) - 1))
        j[list_of_zeros[rand1][0]][list_of_zeros[rand1][1]] = "2"
    else:
        pass


def shifting_r():
    """Shifting right"""

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
    """Adding right"""

    z = 0

    while z < 3:
        x = 0
        for x in range(4):
            y = 3
            while y > 0:
                if j[x][y] != " " and j[x][y] == j[x][y - 1]:
                    j[x][y] = int(j[x][y - 1]) + int(j[x][y])
                    j[x][y] = str(j[x][y])
                    j[x][y - 1] = " "
                y -= 1
            x += 1
        z += 1


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

    z = 0

    while z < 3:
        x = 0
        for x in range(4):
            y = 0
            while y < 3:
                if j[x][y] != " " and j[x][y] == j[x][y + 1]:
                    j[x][y] = int(j[x][y + 1]) + int(j[x][y])
                    j[x][y] = str(j[x][y])
                    j[x][y + 1] = " "

                y += 1
            x += 1
        z += 1


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

    z = 0

    while z < 3:
        y = 0
        for y in range(4):
            x = 3
            while x > 0:
                if j[x][y] != " " and j[x][y] == j[x - 1][y]:
                    j[x][y] = int(j[x - 1][y]) + int(j[x][y])
                    j[x][y] = str(j[x][y])
                    j[x - 1][y] = " "
                x -= 1
            y += 1
        z += 1


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

    z = 0

    while z < 3:
        y = 0
        for y in range(4):
            x = 0
            while x < 3:
                if j[x][y] != " " and j[x][y] == j[x + 1][y]:
                    j[x][y] = int(j[x + 1][y]) + int(j[x][y])
                    j[x][y] = str(j[x][y])
                    j[x + 1][y] = " "
                x += 1
            y += 1
        z += 1


def right():

    shifting_r()
    adding_r()
    shifting_r()
    randomize()


def left():

    shifting_l()
    adding_l()
    shifting_l()
    randomize()


def down():

    shifting_d()
    adding_d()
    shifting_d()
    randomize()


def up():

    shifting_u()
    adding_u()
    shifting_u()
    randomize()


randomize()
randomize()


while True:

    print_table()

    move = input("  ")

    if (move == "w" or move == "W"):
        up()

    if (move == "a" or move == "A"):
        left()

    if (move == "s" or move == "S"):
        down()

    if (move == "d" or move == "D"):
        right()

    if (move == "n" or move == "N"):
        j = [[" ", " ", " ", " "], [" ", " ", " ", " "],
             [" ", " ", " ", " "], [" ", " ", " ", " "]]
        randomize()
        randomize()

    if (move == "g" or move == "G"):
        print()
        print("  Byebye! We hope you enjoyed the game! :)")
        print()
        exit()
