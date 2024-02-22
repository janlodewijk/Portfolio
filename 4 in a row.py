player_1 = input("Enter name of player 1: ")
player_2 = input("Enter name of player 2: ")

current_player = player_1

def initialize_board(rows, cols):
    return [[' ' for _ in range(cols)] for _ in range(rows)]

def display_board(board):
    print(" 1 2 3 4 5 6 7")
    for row in board:
        print("|", "|".join(row), "|", sep="")

# Voor een 4x4 bord zou je het als volgt gebruiken:
rows = 6
cols = 7
board = initialize_board(rows, cols)
display_board(board)

def find_empty_row(board, column):
    for row in range(len(board) - 1, -1, -1):
        if board[row][column] == ' ':
            return row
    return -1  # Geef -1 terug als de kolom vol is

def move(board, player):
    column = int(input(f"{current_player}, Select a column (1-7): ")) - 1
    empty_row = find_empty_row(board, column)

    if empty_row != -1:
        board[empty_row][column] = player
        return column, empty_row
    else:
        print("Column is full. Choose another column.")
        return -1, -1

def victory(board, row, column, player):
    consecutive_count = 0

    for col in range(column, min(column + 4, len(board[0]))):
        if board[row][col] == player:
            consecutive_count += 1
        else:
            consecutive_count = 0

        if consecutive_count == 4:
            return True

    return False

while True:
    if current_player == player_1:
        current_column, current_row = move(board, 'X')  # Player 1's move
        display_board(board)
        if current_row != -1 and victory(board, current_row, current_column, 'X'):
            print(f"Congratulations! {current_player} has won!")
            break
        current_player = player_2

    else:
        current_column, current_row = move(board, 'O')  # Player 2's move
        display_board(board)
        if current_row != -1 and victory(board, current_row, current_column, 'O'):
            print(f"Congratulations! {current_player} has won!")
            break
        current_player = player_1