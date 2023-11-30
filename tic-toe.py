from random import randrange

def display_board(board):
    # Display the Tic-Tac-Toe board
    for row in board:
        for cell in row:
            print(f"| {cell} ", end='')
        print("|\n+---+---+---+")

def enter_move(board):
    # Ask the user for their move and update the board
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                row, col = (move - 1) // 3, (move - 1) % 3
                if board[row][col] != 'O' and board[row][col] != 'X':
                    board[row][col] = 'O'
                    break
                else:
                    print("That square is already occupied. Try again.")
            else:
                print("Please enter a valid number (1-9).")
        except ValueError:
            print("Please enter a valid number (1-9).")

def make_list_of_free_fields(board):
    # Create a list of all free squares on the board
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != 'O' and board[row][col] != 'X':
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    # Check if a player (sign) has won the game
    for row in range(3):
        if all(board[row][col] == sign for col in range(3)):
            return True
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def draw_move(board):
    # Make a random move for the computer (X)
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'

def main():
    board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
    display_board(board)
    
    while True:
        enter_move(board)
        display_board(board)
        
        if victory_for(board, 'O'):
            print("You won!")
            break

        if len(make_list_of_free_fields(board)) == 0:
            print("It's a tie!")
            break

        draw_move(board)
        display_board(board)
        
        if victory_for(board, 'X'):
            print("Computer wins!")
            break

if __name__ == "__main__":
    main()
