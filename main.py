import tictactoe

def main():
    scores = {'Player': 0, 'Computer': 0}

    print("Welcome to Tic-Tac-Toe!")
    print("Choose difficulty: Easy (E), Medium (M), Hard (H)")
    
    while True:
        choice = input("Enter difficulty (E/M/H): ").lower()
        if choice == 'e':
            tictactoe.set_difficulty("easy")
            break
        elif choice == 'm':
            tictactoe.set_difficulty("medium")
            break
        elif choice == 'h':
            tictactoe.set_difficulty("hard")
            break
        else:
            print("Invalid choice! Please enter E, M, or H.")

    while True:
        tictactoe.board = [' ' for _ in range(10)]
        tictactoe.print_board()
        
        while True:
            if tictactoe.winner('O'):
                print("Sorry, you lose!")
                scores['Computer'] += 1
                break

            tictactoe.player_move()
            tictactoe.print_board()

            if tictactoe.winner('X'):
                print("You win!")
                scores['Player'] += 1
                break

            if tictactoe.is_board_full():
                print("It's a tie!")
                break

            move = tictactoe.computer_move()
            if move:
                tictactoe.insert_letter('O', move)
                print(f"Computer placed an O at position {move}:")
                tictactoe.print_board()

            if tictactoe.is_board_full():
                print("It's a tie!")
                break

        print(f"Score - Player: {scores['Player']} | Computer: {scores['Computer']}")

        if not play_again():
            print("Final Score:")
            print(f"Player: {scores['Player']} | Computer: {scores['Computer']}")
            print("Goodbye!")
            break

def play_again():
    while True:
        x = input("Do you want to play again? (y/n): ").lower()
        if x == 'y':
            print('--------------------')
            return True
        elif x == 'n':
            return False
        else:
            print("Invalid input. Enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
