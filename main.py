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
    if user_input not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if user_input not in ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']:
            print("invalid input")
            continue

        if user_input[0] == 'a':
            user_input = int(user_input[1]) + 0
        elif user_input[0] == 'b':
            user_input = int(user_input[1]) + 3
        elif user_input[0] == 'c':
            user_input = int(user_input[1]) + 6

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
