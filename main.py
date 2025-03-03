board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')


current_player = 0
player_symbols = ['x', 'o']

print_board(board)
while True:
    user_input = input("chose your square: ").lower()

    if board[int(user_input) - 1] == ' ':
        board[int(user_input) - 1] = player_symbols[current_player]
    else:
        print("slot already filled")
        continue

    if (
            board[0] == board[1] == board[2] != ' '  # Top row
            or board[3] == board[4] == board[5] != ' '  # Middle row
            or board[6] == board[7] == board[8] != ' '  # Bottom row

            # Vertical win conditions
            or board[0] == board[3] == board[6] != ' '  # Left column
            or board[1] == board[4] == board[7] != ' '  # Middle column
            or board[2] == board[5] == board[8] != ' '  # Right column

            # Diagonal win conditions
            or board[0] == board[4] == board[8] != ' '  # Left-top to right-bottom diagonal
            or board[2] == board[4] == board[6] != ' '  # Right-top to left-bottom diagonal
    ):
        print_board(board)
        print(f"player {player_symbols[current_player]} won")
        break

    if current_player == 0:
        current_player = 1
    elif current_player == 1:
        current_player = 0
    print_board(board)
