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
    return board.count(' ') == 1  # Only one empty space (index 0)

def insert_letter(letter, pos):
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
        try:
            move = int(input("Choose a position (1-9): "))
            if move in range(1, 10) and free_space(move):
                insert_letter('X', move)
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number.")

def select_random(li):
    return random.choice(li)

def computer_move():
    possibles_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    if not possibles_moves:
        return 0  # No moves available

    for let in ['O', 'X']:
        for i in possibles_moves:
            board_copy = board[:]
            board_copy[i] = let
            if winner(board_copy, let):
                return i  # Winning/blocking move

    corners = [i for i in possibles_moves if i in [1, 3, 7, 9]]
    if corners:
        return select_random(corners)

    if 5 in possibles_moves:
        return 5  # Take center if available

    edges = [i for i in possibles_moves if i in [2, 4, 6, 8]]
    if edges:
        return select_random(edges)

    return possibles_moves[0]  # Pick any available move as fallback

def main():
    global board
    board = [' ' for _ in range(10)]
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while not is_board_full():
        if winner(board, 'O'):
            print("Sorry, you lose!")
            break

        player_move()
        print_board()

        if winner(board, 'X'):
            print("You win!")
            break

        move = computer_move()
        if move != 0:
            insert_letter('O', move)
            print(f"Computer placed an O at position {move}:")
            print_board()

        if is_board_full():
            print("It's a tie!")
            break

while True:
    x = input("Do you want to play again? (y/n): ")
    if x.lower() == 'y':
        print('--------------------')
        main()
    else:
        print("Goodbye!")
        break
