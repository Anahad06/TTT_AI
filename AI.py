# Tic Tac Toe AI using the mini-max algo
import random
my_board = {1: ' ', 2: ' ', 3: ' ',4: ' ',5: ' ', 6: ' ',7: ' ', 8:' ', 9:' '}
o_wins = 0 
x_wins = 0
print("Pick between 1-9 for the respective position\n")
print("1, 2, 3\n4, 5, 6\n7, 8, 9\n")

# Symbols 
player = "O"
bot = "X"

while x_wins + o_wins != 1000:
    def draw_board():
        print("")
        print(my_board[1] + "|" + my_board[2] + "|" + my_board[3])
        print("-----")
        print(my_board[4] + "|" + my_board[5] + "|" + my_board[6])
        print("-----")
        print(my_board[7] + "|" + my_board[8] + "|" + my_board[9])
    
    
    def playerMove():
        pos = random.randint(1, 9)
        if my_board[pos] == " ":
            Insert(player, pos, x_wins, o_wins)
    
    def compMove():
        bestScore = -1000 
        bestMove = 0 
        
        for i in my_board.keys():
            if my_board[i] == " ":
                my_board[i] = bot 
                score = miniMax(i, False)
                my_board[i] = " "
                if score > bestScore:
                    bestScore = score
                    bestMove = i
        
        Insert(bot, bestMove, x_wins, o_wins)
        return 
                
    
    def Insert(letter, pos, x_wins, o_wins):
        
        if check_space(pos):
            
            my_board[pos] = letter
    
            if win_condition(letter):
                if letter == "X":
                    print("AI Won!")
                    x_wins += 1
                else:
                    print("Random Move Player Won!")
                    o_wins += 1
            elif draw():
                print("Tie")
                exit()
        
        else:
            pos = random.randint(0, 9)
        
        draw_board()
    
    
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
            
    def check_space(pos):
        if my_board[pos] == " ":
            return True 
        else:
            return False
    
    def draw():
        draw=0
        for i in my_board.keys():
            if my_board[i] != " ":
                draw += 1 
                if draw == 9:
                    print("TIE")
                    exit()
    
    def miniMax(pos, isMax):
        # Terminal States
        if win_condition("X"):
            return 100
        elif win_condition("O"):
            return -100
        elif draw():
            return 0
    
        # Playing
        if isMax:
            bestScore = -1000
    
            for i in my_board.keys():
                # Checks if space is free
                if my_board[i] == " ":
                    my_board[i] = bot
                    score = miniMax(my_board[i], False)
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
                    score = miniMax(my_board[i], True)
                    my_board[i] = " "
                    if score < bestScore:
                        bestScore = score
    
            return bestScore
    
    
    while not check_win():
        compMove()
        playerMove()
    
print("X Wins: ", x_wins)
print("O Wins: ", o_wins)
