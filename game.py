from IPython.display import clear_output

def display_board(board):
    
    clear_output()

    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():

    marker = 'wrong'

    while marker != 'X' and marker != 'O':
        marker = int(input('Player 1 choose either X or O: ')).upper()
    
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')

