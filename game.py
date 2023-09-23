from IPython.display import clear_output
import random

def display_board(board):
    
    #Show board
    clear_output()

    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():

    #Assign X or O to each player
    marker = 'wrong'

    while marker != 'X' and marker != 'O':
        marker = int(input('Player 1 choose either X or O: ')).upper()
    
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')

def player_marker(board, marker, position):

    #Assign either X or O to a specific position on the board
    board[position] = marker

def win_check(board, marker):

    return((board[1] == board[2] == board[3] == marker) or 
    (board[4] == board[5] == board[6] == marker) or 
    (board[7] == board[8] == board[9] == marker) or 
    (board[1] == board[4] == board[7] == marker) or
    (board[2] == board[5] == board[8] == marker) or
    (board[3] == board[6] == board[9] == marker) or 
    (board[1] == board[5] == board[9] == marker) or
    (board[3] == board[5] == board[7] == marker))

def choose_first():
    player1 = 1
    player2 = 2

    #Decide who goes first
    turn = random.randint(1,2)

    if turn == player1:
        return 'Player1'
    elif turn == player2: 
        return 'Player2'

def space_check(board, position):

    #Check to see if the position is available for play
    return board[position] == ' '

def full_board(board):

    #Checks to see if the board is full
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose a position: (1-9)'))
    
    return position

def replay():
    
    play_again = input('Would you like to play again? (Y or N)').upper()
    
    return play_again == 'Y'

