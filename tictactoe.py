import random

board = [' ' for _ in range(10)]

def print_board():
    print("\n")
    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")
    print("\n")

def is_board_full():
    return ' ' not in board[1:]  

def insert_letter(letter, pos):
    board[pos] = letter

def free_space(pos):
    return board[pos] == ' '

def winner(l, board_copy=None):
    """
    Checks if the given letter ('X' or 'O') has won.
    If board_copy is provided, checks for that board state instead of the global board.
    """
    b = board if board_copy is None else board_copy
    return (
        (b[1] == l and b[2] == l and b[3] == l) or
        (b[4] == l and b[5] == l and b[6] == l) or
        (b[7] == l and b[8] == l and b[9] == l) or
        (b[1] == l and b[4] == l and b[7] == l) or
        (b[2] == l and b[5] == l and b[8] == l) or
        (b[3] == l and b[6] == l and b[9] == l) or
        (b[1] == l and b[5] == l and b[9] == l) or
        (b[3] == l and b[5] == l and b[7] == l)
    )

def player_move():
    while True:
        move = input("Choose a position (1-9) or type 'exit' to quit: ").lower()
        if move == "exit":
            return "exit"
        if move.isdigit():
            move = int(move)
            if move in range(1, 10) and free_space(move):
                insert_letter('X', move)
                return move
        print("Invalid move! Try again.")

def quit_game(scores):
    print(f"Final Score: Player {scores['Player']} - {scores['Computer']} Computer")
    print("Thanks for playing! Goodbye!")
    exit()

def select_random(li):
    return random.choice(li)

def computer_move():
    possible_moves = [x for x in range(1, 10) if free_space(x)]

    for let in ['O', 'X']:  
        for i in possible_moves:
            board_copy = board[:]  
            board_copy[i] = let
            if winner(let, board_copy):  
                return i

    if 5 in possible_moves:  
        return 5

    corners = [i for i in possible_moves if i in [1, 3, 7, 9]]
    if corners:
        return select_random(corners)

    edges = [i for i in possible_moves if i in [2, 4, 6, 8]]
    if edges:
        return select_random(edges)

    return None  
