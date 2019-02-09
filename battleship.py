# A mini, one-player version of the game 'Battleship'. Written by following along with the Python tutorial on Codecademy.
# Original code updated from Python2 to Python3 by Wesley Swafford.

from random import randint

def battleship():

    board = []

    for x in range(5):
        board.append(["O"] * 5)

    def print_board(board):
        for row in board:
            print(" ".join(row))

    
    print("\nLet's play Battleship!\n")
    
    print_board(board)

    def random_row(board):
        return randint(1, len(board))

    def random_col(board):
        return randint(1, len(board[0]))

    ship_row = random_row(board)
    ship_col = random_col(board)
    # These two lines below are used to show the location of the 'ship' for debugging.
    #print ship_row
    #print ship_col

    turn = 0
    for turn in range(99):
        
        print("\nTurn %s" % str(turn + 1))
        
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))

        if guess_row == ship_row and guess_col == ship_col:
            print
            print("Congratulations! You sank my battleship!")
            print
            board[guess_row - 1][guess_col - 1] = "#"
            print_board(board)
            break
        else:
            if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
                print
                print("Oops, that's not even in the ocean.")
                print
                print_board(board)
                # Commented lines below can be used to limit guesses
                #if turn == 3:
                    #break
            elif (board[guess_row - 1][guess_col - 1] == "X"):
                print
                print("You guessed that one already.")
                print
                print_board(board)
            
            else:
                print
                print("You missed my battleship!")
                print
                board[guess_row - 1][guess_col - 1] = "X"
                turn + 1
                # Commented lines below can be used to limit guesses
                #if turn == 3:
                    #print_board(board)
                    #break
                print_board(board)
    

    print
    print("Game Over")
    print
    replay_answer = input("Would you like to Play again? Y/N ")
    print
    replay_answer = replay_answer.lower()
    if replay_answer == "y":
        battleship()

battleship()
