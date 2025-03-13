import random

board = [' ' for _ in range(10)]

def print_board():
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

def is_board_full():
    return ' ' not in board[1:]  
 

def insert_letter(letter, pos):
    global board
    board[pos] = letter


def free_space(pos):
    return board[pos] == ' '

def winner(board, l):
    return (
        (board[1] == l and board[2] == l and board[3] == l) or
        (board[4] == l and board[5] == l and board[6] == l) or
        (board[7] == l and board[8] == l and board[9] == l) or
        (board[1] == l and board[4] == l and board[7] == l) or
        (board[2] == l and board[5] == l and board[8] == l) or
        (board[3] == l and board[6] == l and board[9] == l) or
        (board[1] == l and board[5] == l and board[9] == l) or
        (board[3] == l and board[5] == l and board[7] == l)
    )

def player_move():
    while True:
        move = input("Choose a position (1-9): ")
        if move.isdigit():
            move = int(move)
            if move in range(1, 10) and free_space(move):
                insert_letter('X', move)
                break
        print("Invalid move! Try again.")


def select_random(li):
    return random.choice(li)

def computer_move():
    possible_moves = [x for x in range(1, 10) if free_space(x)]

    for let in ['O', 'X']:  # Check winning or blocking move
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if winner(board_copy, let):
                return i

    if 5 in possible_moves:  # Prioritize center
        return 5

    corners = [i for i in possible_moves if i in [1, 3, 7, 9]]
    if corners:
        return select_random(corners)

    edges = [i for i in possible_moves if i in [2, 4, 6, 8]]
    if edges:
        return select_random(edges)

    return possible_moves[0]  # Last resort
 
