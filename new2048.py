import os
import random


j = [[" ", " ", " ", " "], [" ", " ", " ", " "],
     [" ", " ", " ", " "], [" ", " ", " ", " "]]


def print_table():
    x = "|", j[0][0], "|", j[0][1],  "|", j[0][2], "|", j[0][3],  "|"
    row_length = len(x)
    line = "-" * row_length
    print(*line)
    for n in j:
        print("|", n[0], "|", n[1],  "|", n[2], "|", n[3],  "|")
        print(*line)


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

randomize()
#randomize()

print_table()

shifting_r()

#print_table()
