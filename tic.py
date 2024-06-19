def draw_board(board):
    print("----------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(cell, end=" |")
        print("\n", end="")
        print("----------")

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player) or \
           (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            return True

    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True

    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

    print("\nHey Hii!! Let's have some fun playing Tic-Tac-Toe!!")
    print("To start the game press S or s")
    start = input()

    if start.upper() == 'S':
        print("Let's Start!!")
        print("The column and row numbers are 0, 1 and 2. Please select the box with the appropriate values!! ")
        print("   (to select first box of first row, enter 0 0")
        print("    to select first box of second row, enter 0 1")
        print("    to select last box of last row, enter 2 2)")
        print(" Proceed accordingly")
    else:
        print("Seems you don't want to play now. Comeback when you are free!!")
        return
    

    while not game_over:
        draw_board(board)
        print(f"Player {current_player}, enter row and column (0-2): ", end="")
        row, col = map(int, input().split())

        if board[row][col] == ' ':
            board[row][col] = current_player
            game_over = check_win(board, current_player)

            if game_over:
                draw_board(board)
                print("                        GAME OVER!!!!")
                print(f"                        Player {current_player} wins!  Congratulations!!!")
                print()
            elif check_draw(board):
                draw_board(board)
                print("                        GAME OVER!!!!")
                print("                        It's a DRAWW!")
                print()
                game_over = True

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That spot is already taken. Try again.")

if __name__ == "__main__":
    main()