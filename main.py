import tictactoe as XO

def main():
    XO.board = [' ' for _ in range(10)]  # Update XO's board reference
    print("Welcome to Tic-Tac-Toe!")
    XO.print_board()

    while True:
        if XO.winner(XO.board, 'O'):
            print("Sorry, you lose!")
            break

        XO.player_move()
        XO.print_board()

        if XO.winner(XO.board, 'X'):
            print("You win!")
            break

        if XO.is_board_full():
            print("It's a tie!")
            break

        move = XO.computer_move()
        if move:
            XO.insert_letter('O', move)
            print(f"Computer placed an O at position {move}:")
            XO.print_board()

        if XO.is_board_full():
            print("It's a tie!")
            break

    play_again()


def play_again():
    while True:
        x = input("Do you want to play again? (y/n): ").lower()
        if x == 'y':
            print('--------------------')
            main()
        elif x == 'n':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Enter 'y' or 'n'.")



if __name__ == "__main__":
    main()
    
