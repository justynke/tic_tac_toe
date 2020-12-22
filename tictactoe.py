def check_winner_x():
    # print("executed {}, {}, {}".format(x,y,z))
    if (tictac[0][0] == "X") & (tictac[0][1] == "X") & (tictac[0][2] == "X"):   # przerobić te funkcje na tictac
        return True
    elif (tictac[0][0] == "X") & (tictac[1][1] == "X") & (tictac[2][2] == "X"):
        return True
    elif (tictac[1][0] == "X") & (tictac[1][1] == "X") & (tictac[1][2] == "X"):
        return True
    elif (tictac[2][0] == "X") & (tictac[2][1] == "X") & (tictac[2][2] == "X"):
        return True
    elif (tictac[0][2] == "X") & (tictac[1][1] == "X") & (tictac[2][0] == "X"):
        return True
    elif (tictac[0][0] == "X") & (tictac[1][0] == "X") & (tictac[2][0] == "X"):
        return True
    elif (tictac[0][1] == "X") & (tictac[1][1] == "X") & (tictac[2][1] == "X"):
        return True
    elif (tictac[0][2] == "X") & (tictac[1][2] == "X") & (tictac[2][2] == "X"):
        return True


def check_winner_o():
    # print("executed {}, {}, {}".format(x,y,z))
    if (tictac[0][0] == "O") & (tictac[0][1] == "O") & (tictac[0][2] == "O"):   # przerobić te funkcje na tictac
        return True
    elif (tictac[0][0] == "O") & (tictac[1][1] == "O") & (tictac[2][2] == "O"):
        return True
    elif (tictac[1][0] == "O") & (tictac[1][1] == "O") & (tictac[1][2] == "O"):
        return True
    elif (tictac[2][0] == "O") & (tictac[2][1] == "O") & (tictac[2][2] == "O"):
        return True
    elif (tictac[0][2] == "O") & (tictac[1][1] == "O") & (tictac[2][0] == "O"):
        return True
    elif (tictac[0][0] == "O") & (tictac[1][0] == "O") & (tictac[2][0] == "O"):
        return True
    elif (tictac[0][1] == "O") & (tictac[1][1] == "O") & (tictac[2][1] == "O"):
        return True
    elif (tictac[0][2] == "O") & (tictac[1][2] == "O") & (tictac[2][2] == "O"):
        return True


def druck():
    print("---------")
    print("|", end=" ")
    for x in range(3):
        print(tictac[0][x], end=" ")
    print("|")

    print("|", end=" ")
    for x in range(3):
        print(tictac[1][x], end=" ")
    print("|")

    print("|", end=" ")
    for x in range(3):
        print(tictac[2][x], end=" ")
    print("|")
    print("---------")


def enter_coordinates():
    while True:
        x, y = input("Enter the coordinates: ").split()
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print("You should enter numbers!")
        else:
            if x > 3 or x < 1 or y > 3 or y < 1:
                print("Coordinates should be from 1 to 3!")
            else:
                if (tictac[x - 1][y - 1] == "O") or (tictac[x - 1][y - 1] == "X"):
                    print("This cell is occupied! Choose another one!")
                else:
                    return x, y


def insert_x(x, y):
    tictac[x-1][y-1] = "X"


def insert_o(x, y):
    tictac[x-1][y-1] = "O"


def check_amount():
    xs = 0
    os = 0
    for i in range(len(tictac)):
        for j in range(len(tictac[i])):
            if(tictac[i][j]) == "X":
                xs += 1
            elif(tictac[i][j]) == "O":
                os += 1
    if (xs-os >= 2) or (os-xs >= 2):
        print("Impossible")
        exit()


def check_not_finished():
    if any(" " in sublist for sublist in tictac):
        return True
    else:
        return False

# POCZĄTEK GRY
#
#
#


tictac = [[" " for x in range(3)] for y in range(3)]
druck()

x_on_move = 0
while True:
    x, y = enter_coordinates()
    if x_on_move % 2 == 0:
        insert_x(x, y)
    else:
        insert_o(x, y)
    druck()

#      SPRAWDZANIE, CZY GRA SIE ZAKONCZYLA
    check_amount()
    if check_winner_o() and check_winner_x():
        print("Impossible")
        exit()

    if check_winner_o():
        print("O wins")
        exit()

    if check_winner_x():
        print("X wins")
        exit()

    if check_not_finished():
        print("Game not finished")
    else:
        print("Draw")
        exit()
    x_on_move += 1
