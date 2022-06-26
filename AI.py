import random

my_board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
print("Pick between 1-9 for the respective position\n")
print("1, 2, 3\n4, 5, 6\n7, 8, 9\n")

# Symbols
player = "O"
bot = "X"


def draw_board():
    print("")
    print(my_board[1] + "|" + my_board[2] + "|" + my_board[3])
    print("-----")
    print(my_board[4] + "|" + my_board[5] + "|" + my_board[6])
    print("-----")
    print(my_board[7] + "|" + my_board[8] + "|" + my_board[9])


def check_win():
    # Hor Check
    if my_board[1] == my_board[2] and my_board[2] == my_board[3] and my_board[3] != " ":
        return True
    elif my_board[4] == my_board[5] and my_board[5] == my_board[6] and my_board[6] != " ":
        return True
    elif my_board[7] == my_board[8] and my_board[8] == my_board[9] and my_board[9] != " ":
        return True

    # Ver Check
    elif my_board[1] == my_board[4] and my_board[4] == my_board[7] and my_board[7] != " ":
        return True
    elif my_board[2] == my_board[5] and my_board[5] == my_board[8] and my_board[8] != " ":
        return True
    elif my_board[3] == my_board[6] and my_board[6] == my_board[9] and my_board[9] != " ":
        return True

        # Dia Check
    elif my_board[1] == my_board[5] and my_board[5] == my_board[9] and my_board[9] != " ":
        return True
    elif my_board[3] == my_board[5] and my_board[5] == my_board[7] and my_board[7] != " ":
        return True

    # If No Win Condition Satisfied then...
    else:
        return False


def win_condition(mark):
    # Horizontal Win Condition Check
    if my_board[1] == my_board[2] and my_board[2] == my_board[3] and my_board[1] == mark:
        return True
    elif my_board[4] == my_board[5] and my_board[5] == my_board[6] and my_board[4] == mark:
        return True
    elif my_board[7] == my_board[8] and my_board[8] == my_board[9] and my_board[7] == mark:
        return True

    # Vertical Win Condition Check
    if my_board[1] == my_board[4] and my_board[4] == my_board[7] and my_board[1] == mark:
        return True
    elif my_board[2] == my_board[5] and my_board[5] == my_board[8] and my_board[2] == mark:
        return True
    elif my_board[3] == my_board[6] and my_board[6] == my_board[9] and my_board[3] == mark:
        return True

    # Diagonal Win Conditions
    if my_board[3] == my_board[5] and my_board[5] == my_board[7] and my_board[3] == mark:
        return True
    elif my_board[1] == my_board[5] and my_board[5] == my_board[9] and my_board[1] == mark:
        return True
    else:
        return False


def draw():
    draw = 0
    for i in my_board.keys():
        if my_board[i] != " ":
            draw += 1
            if draw == 9:
                print("TIE")
                exit()


def space_free(pos):
    for i in my_board.keys():
        if i == pos:
            if my_board[i] == " ":
                return True
            else:
                return False


def Insert(mark: object, pos: object) -> object:
    if space_free(pos):

        my_board[pos] = mark

        if win_condition(mark):
            if mark == "X":
                print("AI Won!")
            else:
                print("Random Move Player Won!")
        elif draw():
            print("Tie")
            exit()

    else:
        if mark == "O":
            pos = int(input("Enter New Position:"))
            Insert(mark, pos)

    draw_board()


def playerMove():
    pos = int(input("Position: "))
    Insert(player, pos)


def compMove() -> object:
    bestScore = -1
    bestMove = 0

    for keys in my_board.keys():
        if my_board[keys] == " ":
            my_board[keys] = bot
            score = minMax(keys, True)
            my_board[keys] = " "
            if score > bestScore:
                bestMove = keys
                bestScore = score

    Insert(bot, bestMove)


def minMax(pos, isMax):
    # Terminal States
    if win_condition(bot):
        return 1
    elif win_condition(player):
        return -1
    elif draw():
        return 0

    if isMax:
        bestScore = -1000

        for keys in my_board.keys():
            if my_board[keys] == " ":
                my_board[keys] = bot
                score = minMax(keys, False)
                my_board[keys] = " "
                if score > bestScore:
                    bestScore = score

        return bestScore

    else:
        bestScore = 800

        for keys in my_board.keys():
            if my_board[keys] == " ":
                my_board[keys] = bot
                score = minMax(keys, True)
                my_board[keys] = " "
                if score < bestScore:
                    bestScore = score

        return bestScore


while not check_win():
    compMove()
    playerMove()
