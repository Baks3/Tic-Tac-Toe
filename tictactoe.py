


def print_board():
    board = [' ' for i in range(10)]

    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def insert_letter(letter,pos,board):
    board[pos] = letter

def free_space(pos, board):
    return board[pos] == ' '


def winner(board,l):
    return ((board[1] == l and board[2] == l and board[3] == l) or
    (board[4] == l and board[5] == l and board[6] == l) or
    (board[7] == l and board[8] == l and board[9] == l) or
    (board[1] == l and board[4] == l and board[7] == l) or
    (board[2] == l and board[5] == l and board[8] == l) or
    (board[3] == l and board[6] == l and board[9] == l) or
    (board[1] == l and board[5] == l and board[9] == l) or
    (board[3] == l and board[5] == l and board[7] == l))

print("Welcome to the game!")
print_board()

while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        print('--------------------')
        print("Welcome to the game!")
        print_board()
    else:
        print("Goodbye!")
        break

   