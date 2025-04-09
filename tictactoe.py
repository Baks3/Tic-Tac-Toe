import random

board = [' ' for _ in range(10)]
difficulty = "medium"  # Default difficulty

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

def print_position_guide():
    print("Position Guide:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 \n")

def is_board_full(board_state=None):
    b = board_state if board_state else board
    return ' ' not in b[1:]

def insert_letter(letter, pos):
    board[pos] = letter

def free_space(pos, board_state=None):
    b = board_state if board_state else board
    return b[pos] == ' '

def winner(l, board_state=None):
    b = board_state if board_state else board
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

def select_random(li):
    return random.choice(li)

def set_difficulty(level):
    global difficulty
    difficulty = level

def player_move():
    while True:
        move = input("Choose a position (1-9) or type 'exit' or 'quit' to leave the game: ").lower()
        if move in ['exit', 'quit']:
            quit_game()
        if move.isdigit():
            move = int(move)
            if move in range(1, 10) and free_space(move):
                insert_letter('X', move)
                break
        print("Invalid move! Try again.")

def quit_game():
    print("Thanks for playing! Goodbye!")
    exit()

def computer_move():
    if difficulty == "easy":
        return easy_move()
    elif difficulty == "medium":
        return medium_move()
    elif difficulty == "hard":
        return minimax_move()

def easy_move():
    possible_moves = [x for x in range(1, 10) if free_space(x)]
    return select_random(possible_moves)

def medium_move():
    possible_moves = [x for x in range(1, 10) if free_space(x)]

    # Try to win or block
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

def minimax(board_state, depth, is_maximizing):
    scores = {'O': 10, 'X': -10, 'tie': 0}

    if winner('O', board_state):
        return scores['O']
    if winner('X', board_state):
        return scores['X']
    if is_board_full(board_state):
        return scores['tie']

    if is_maximizing:
        best_score = -float('inf')
        for i in range(1, 10):
            if free_space(i, board_state):
                board_state[i] = 'O'
                score = minimax(board_state, depth + 1, False)
                board_state[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(1, 10):
            if free_space(i, board_state):
                board_state[i] = 'X'
                score = minimax(board_state, depth + 1, True)
                board_state[i] = ' '
                best_score = min(score, best_score)
        return best_score

def minimax_move():
    best_score = -float('inf')
    best_move = None
    for i in range(1, 10):
        if free_space(i):
            board[i] = 'O'
            score = minimax(board[:], 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move
