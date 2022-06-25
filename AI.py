# Random
import random

# Dictonary to replicate the 9 possible outcomes
my_board = {1: " ", 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
print("\n1, 2, 3\n4, 5, 6\n7, 8, 9\nThese values represent the board when asked for Player Position.\n")

# Draws The Board
def draw_board(my_board):
    print("\n"+my_board[1] + "|" + my_board[2] + '|' + my_board[3])
    print(my_board[4] + "|" + my_board[5] + '|' + my_board[6])
    print(my_board[7] + "|" + my_board[8] + '|' + my_board[9])

def check_space(pos):
    # Checks if space is free
    if my_board[pos] == " ":
        # Space is free = True
        return True
    else:
        # Space is not free = False
        return False
def check_win():
    # Horizontal Win Condition Check
    if my_board[1] == my_board[2] and my_board[2] == my_board[3] and my_board[1] != " ":
        return True
    elif my_board[4] == my_board[5] and my_board[5] == my_board[6] and my_board[4] != " ":
        return True
    elif my_board[7] == my_board[8] and my_board[8] == my_board[9] and my_board[7] != " ":
        return True

    # Vertical Win Condition Check
    if my_board[1] == my_board[4] and my_board[4] == my_board[7] and my_board[1] != " ":
        return True
    elif my_board[2] == my_board[5] and my_board[5] == my_board[8] and my_board[2] != " ":
        return True
    elif my_board[3] == my_board[6] and my_board[6] == my_board[9] and my_board[3] != " ":
        return True

    # Diagonal Win Conditions
    if my_board[3] == my_board[5] and my_board[5] == my_board[7] and my_board[3] != " ":
        return True
    elif my_board[1] == my_board[5] and my_board[5] == my_board[9] and my_board[1] != " ":
        return True
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


def tie():
    val = 0
    for i in my_board.keys():
        if i != " ":
            val += 1
            if val == 9:
                return True
            else:
                return False

def enterLetter(pos, letter):
    global val
    val = 0
    # If Space is free
    if check_space(pos):

        # Then put the letter for the index value
        my_board[pos] = letter

        val += 1

        # Draw the board
        draw_board(my_board)

        if check_win():
            if letter == "X":
                print("Bot Wins!")
                exit()
            else:
                print("Player Wins!")
                exit()

        elif tie():
            print("Tie")
            exit()
    else:
        if letter == "X":
            pos = int(input("Enter New Position:"))
        else:
            pos = random.randint(1, 9)

            if my_board[pos] == " ":
                enterLetter(pos, letter)
player = 'O'
bot = 'X'

def randomMove() -> object:
    pos = random.randint(0, 9)
    enterLetter(pos, player)

def computerMove():
    bestScore = -1000
    bestMove = 0

    for i in my_board.keys():
        # Checks if space is free
        if my_board[i] == " ":
            my_board[i] = bot
            score = minimax(my_board, False)
            my_board[i] = " "
            if score > bestScore:
                bestScore = score
                bestMove = i

    enterLetter(bestMove, bot)

def minimax(my_board, isMax):

    # Terminal States
    if win_condition(bot):
        return 100

    elif win_condition(player):
        return -100

    elif tie():
        return 0

    # Playing
    if isMax:
        bestScore = -1000

        for i in my_board.keys():
            # Checks if space is free
            if my_board[i] == " ":
                my_board[i] = bot
                score = minimax(my_board, False)
                my_board[i] = " "
                if score > bestScore:
                    bestScore = score

        return bestScore

    else:
        bestScore = 800

        for i in my_board.keys():
            # Checks if space is free
            if my_board[i] == " ":
                my_board[i] = bot
                score = minimax(my_board, True)
                my_board[i] = " "
                if score < bestScore:
                    bestScore = score

        return bestScore



while not check_win():
    computerMove()
    randomMove()


draw_board(my_board)
