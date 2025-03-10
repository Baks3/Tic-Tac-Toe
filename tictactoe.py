
board = [' ' for i in range(10)]

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
    if board.count(' ') > 1:
        return False
    else:
        return True

def insert_letter(letter,pos):
    board[pos] = letter

def free_space(pos):
    return board[pos] == ' '


def player_move():
    while True:
        try:
            pos = int(input("Choose a position (1-9): "))
            if pos in range(1, 10) and free_space(pos):
                insert_letter('X', pos)
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number.")

def winner(board,l):
    return ((board[1] == l and board[2] == l and board[3] == l) or
    (board[4] == l and board[5] == l and board[6] == l) or
    (board[7] == l and board[8] == l and board[9] == l) or
    (board[1] == l and board[4] == l and board[7] == l) or
    (board[2] == l and board[5] == l and board[8] == l) or
    (board[3] == l and board[6] == l and board[9] == l) or
    (board[1] == l and board[5] == l and board[9] == l) or
    (board[3] == l and board[5] == l and board[7] == l))

def player_move():
    run = True
    while run:
        move = input("please select a position to enter the X between 1 to 9")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if free_space(move):
                    run = False
                    insert_letter('X' , move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')

        except:
            print('Please type a number')

def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def computer_move():
    possibles_moves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibles_moves:
            board_copy = board[:]
            board_copy[i] = let
            if winner(board_copy, let):
                move = i
                return move

    corners_open = []
    for i in possibles_moves:
        if i in [1 , 3 , 7 , 9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    if 5 in possibles_moves:
        move = 5
        return move

    edges_open = []
    for i in possibles_moves:
        if i in [2,4,6,8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)
        return move

print("Welcome to the game!")
print_board()

def main():
    print("Welcome to the game!")
    print_board()

    while not(is_board_full()):
        if not(winner(board , 'O')):
            player_move()
            print_board()
        else:
            print("sorry you loose!")
            break

        if not(winner(board , 'X')):
            move = computer_move()
            if move == 0:
                print(" ")
            else:
                insert_letter('O' , move)
                print('computer placed an o on position' , move , ':')
                print_board()
        else:
            print("you win!")
            break

    if is_board_full():
        print("Tie game")

while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        print('--------------------')
        print("Welcome to the game!")
        print_board()
    else:
        print("Goodbye!")
        break

   