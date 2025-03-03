board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player_symbols = ['x', 'o']
current_player = 0

def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')


def is_valid_input(user_input):
    """Validates if input is a valid number or coordinate."""
    return user_input in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

def convert_to_number(user_input):
    """Converts coordinate input to board index."""
    if user_input[0] == 'a':
        return int(user_input[1]) - 1
    elif user_input[0] == 'b':
        return int(user_input[1]) + 2
    elif user_input[0] == 'c':
        return int(user_input[1]) + 5
    return int(user_input) - 1

def check_win(board):
    """Checks if a player has won the game."""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    return False


print_board(board)
while True:
    user_input = input("Choose your square: ").lower()

    if not is_valid_input(user_input):
        print("Invalid input")
        continue

    board_position = convert_to_number(user_input)

    if board[board_position] == ' ':
        board[board_position] = player_symbols[current_player]
    else:
        print("Slot already filled")
        continue

    if check_win(board):
        print_board(board)
        print(f"Player {player_symbols[current_player]} won!")
        break

    current_player = 1 - current_player  # Switch players
    print_board(board)
