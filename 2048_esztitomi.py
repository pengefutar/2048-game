
# Welcome to Eszti and Tomi's 2048 code! :)


# Importing the important modules for the game

import os
import random


# This is the starting table

a = [0] * 4
b = [0] * 4
c = [0] * 4
d = [0] * 4


# We saved a losing and a winning table too for testing. 
# Press down(s) at the first one to lose, and
# press left(a) at the second one to win.

'''
a=[4, 8, 16, 32]
b=[64, 128, 256, 8]
c=[8, 4, 2, 4]
d=[8, 2, 4, 2]
'''
'''
a=[1024, 1024, 0, 0]
b=[0] * 4
c=[0] * 4
d=[0] * 4
'''

# Making one list of the four different ones above (lists in a list)

j = [a,b,c,d]



###################################################################



# Credits :D and instructions.
# Originally we wanted Q to be the quit option,
# but it's right next to the WASD, so it would be impractical.

def madeby():
    print()
    print("  M    M    AA    DDDDD    EEEEEE        BBBBB  YY    YY ")
    print("  MM  MM   A  A   D   DD   EE            BB   B  YY  YY  ")
    print("  M MM M  AAAAAA  D    DD  EEEE          BBBBB     YY    ")
    print("  M    M  A    A  D   DD   EE            BB   B    YY    ")
    print("  M    M  A    A  DDDDD    EEEEEE        BBBBB     YY    ")
    print()
    print()
    print("  EEEEEE  SSSSSS  ZZZZZZ  TTTTTT  II         AA    N    N  DDDDD         TTTTTT   OOOO   M    M   II ")
    print("  EE      SS         ZZ     TT    II        A  A   NN   N  D   DD          TT    OO  OO  MM  MM   II ")
    print("  EEEE    SSSSSS    ZZ      TT    II       AAAAAA  N N  N  D    DD         TT    OO  OO  M MM M   II ")
    print("  EE          SS   ZZ       TT    II       A    A  N  N N  D   DD          TT    OO  OO  M    M   II ")
    print("  EEEEEE  SSSSSS  ZZZZZZ    TT    II       A    A  N   NN  DDDDD           TT     OOO0   M    M   II ")
    print()
    print()
    print("  Use WASD to shift")
    print("  Press N to start a new game")
    print("  Press G to give up")
    print()


# Shifting the numbers right

def shifting_r(x):
    mm = 3
    while mm > 0:
        m = 3
        while m > 0:
            if x[m] == 0:
                x[m] = x[m-1]
                x[m-1] = 0
            m -= 1
        mm -= 1


# Shifting left

def shifting_l(x):
    mm = 0
    while mm < 3:
        m = 0
        while m < 3:
            if x[m] == 0:
                x[m] = x[m+1]
                x[m+1] = 0
            m += 1
        mm += 1


# Shifting down

def shifting_d():
    g = 0
    while g <= 3:
        f = 3
        while f > 0:
            if d[g] == 0:
                d[g] = c[g]
                c[g] = 0

            if c[g] == 0:
                c[g] = b[g]
                b[g] = 0

            if b[g] == 0:
                b[g] = a[g]
                a[g] = 0
            f -= 1
        g += 1


# Shifting up

def shifting_u():
    g = 0
    while g <= 3:
        f = 3
        while f > 0:
            if a[g] == 0:
                a[g] = b[g]
                b[g] = 0

            if b[g] == 0:
                b[g] = c[g]
                c[g] = 0

            if c[g] == 0:
                c[g] = d[g]
                d[g] = 0
            f -= 1
        g += 1



###################################################################



# Adding the same numbers next to each other to the right

def adding_r(x):
    p = 3
    while p > 0:
        if x[p] == x[p-1]:      
            x[p] = x[p-1] + x[p]
            x[p-1] = 0
        p -= 1


# Adding left

def adding_l(x):
    p = 0
    while p < 3:
        if x[p] == x[p+1]:
            x[p] = x[p+1] + x[p]
            x[p+1] = 0
        p += 1


# Adding down

def adding_d():
    g = 0
    while g <= 3:
        if d[g] == c[g]:
            d[g] = d[g] + c[g]
            c[g] = 0

        if c[g] == b[g]:
            c[g] = c[g] + b[g]
            b[g] = 0

        if b[g] == a[g]:
            b[g] = b[g] + a[g]
            a[g] = 0
        g += 1


# Adding up

def adding_u():
    g = 3
    while g >= 0:
        if a[g] == b[g]:
            a[g] = a[g] + b[g]
            b[g] = 0

        if b[g] == c[g]:
            b[g] = b[g] + c[g]
            c[g] = 0

        if c[g] == d[g]:
            c[g] = c[g] + d[g]
            d[g] = 0
        g -= 1



###################################################################


# We call the checksame function when there are no more zeros in the table.
# It checks if there are possible moves (same numbers next to each other),
# and if there aren't, a nice message pops up, and the game quits.
# An empty list is generated for the pairs. 
# The operation fills it up with a 1 every time it finds one.
# If there is something in the list, the game continues, 
# but if the list stays empty, we lose. 

def checksame():
    lose = False
    same = []
    i = 0

    mm = 3
    while mm > 0:
        m = 3
        while m > 0:
            if a[m] == a[m-1]:
                same.append(1)
            if b[m] == b[m-1]:
                same.append(1)
            if c[m] == c[m-1]:
                same.append(1)
            if d[m] == d[m-1]:
                same.append(1)
            m -= 1
        mm -= 1

    if same == []:
        lose = True

    if lose == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        madeby()

        for n in j:
            print('\033[1m  {0:5d}{1:5d}{2:5d}{3:5d}\x1b[0m'.format(n[0], n[1], n[2], n[3]))
            print()

        print()
        print("  YOU LOSE, BITCH")
        print()
        exit()

        

###################################################################


# We list what happens if the user decides to press left or right.
# First we need shifting, then adding, and after that we need another shifting,
# because there are possible scenarios where some zeros are at wrong places.

def right():
    global a
    shifting_r(a)
    adding_r(a)
    shifting_r(a)

    global b
    shifting_r(b)
    adding_r(b)
    shifting_r(b)

    global c
    shifting_r(c)
    adding_r(c)
    shifting_r(c)

    global d
    shifting_r(d)
    adding_r(d)
    shifting_r(d)


def left():
    global a
    shifting_l(a)
    adding_l(a)
    shifting_l(a)

    global b
    shifting_l(b)
    adding_l(b)
    shifting_l(b)

    global c
    shifting_l(c)
    adding_l(c)
    shifting_l(c)

    global d
    shifting_l(d)
    adding_l(d)
    shifting_l(d)



###################################################################



# Function to generate random 2s in the table. 
# It collects the coordinates of the zeros, and 
# randomly chooses one of them.

def randomize():

    list_of_zeros = []

    g = 0
    while g <= 3:
        f = 3
        while f >= 0:
            if j[g][f] == 0:
                list_of_zeros.append( (g,f) )
            f -= 1
        g += 1
    
    if list_of_zeros != []:
        rand1 = (random.randint(0, len(list_of_zeros)-1))
        j[list_of_zeros[rand1][0]][list_of_zeros[rand1][1]] = 2
    else:
        pass



###################################################################     



# At start two 2s are generated in the board

randomize() 
randomize()


# This is a "forever" loop for running the game continusly

while True: 

    os.system('cls' if os.name == 'nt' else 'clear') 
    
    madeby()

    # Printing the table for every steps

    for n in j: 
        print('\033[1m  {0:5d}{1:5d}{2:5d}{3:5d}\x1b[0m'.format(n[0], n[1], n[2], n[3]))
        print()

    print()

    move = input("  ")

    # Moving the numbers up

    if (move == "w" or 
    move == "W"):
        shifting_u()
        adding_u()
        shifting_u()
        randomize()
  
    # Moving the nubers left

    if (move == "a" or 
    move == "A"):
        left()
        randomize()

    # Moving the numbers down

    if (move == "s" or 
    move == "S"):
        shifting_d()
        adding_d()
        shifting_d()
        randomize()

    # Moving the numbers right

    if (move == "d" or 
    move == "D"):
        right()
        randomize()

    # New game

    if (move == "n" or
    move == "N"):
        a = [0] * 4
        b = [0] * 4
        c = [0] * 4
        d = [0] * 4
        j = [a,b,c,d]
        randomize()
        randomize()

    # Give up

    if (move == "g" or
    move == "G"):
        print()
        print("  Byebye! We hope you enjoyed the game! :)")
        print()
        exit()

    # Checking the winning condition, 
    # and if the result is positive we print a message and quit.

    if (2048 in a or
        2048 in b or
        2048 in c or
        2048 in d):

        os.system('cls' if os.name == 'nt' else 'clear')
        madeby()

        for n in j:
            print('\033[1m  {0:5d}{1:5d}{2:5d}{3:5d}\x1b[0m'.format(n[0], n[1], n[2], n[3]))
            print()
            
        print()
        print("  CONGRATULATIONS! YOU WON!")
        print("  YOU'RE AWESOME!! :D")
        print()
        exit()

    # Ckecking if there are any zeros left,
    # if there aren't, we call the checksame function.

    if (0 not in a and
        0 not in b and
        0 not in c and
        0 not in d):
        checksame()
