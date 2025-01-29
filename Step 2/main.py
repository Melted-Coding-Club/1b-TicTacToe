board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')


# Defines the current player. 0 is x and 1 is o. This is because numbers are easier to deal with than x and o
current_player = 0
# By making the players 0 and 1, we can give them any symbol
# player_symbols defines the players' Symbols. This means player_symbols[0] is x and [1] is o
player_symbols = ['x', 'o']

# Print our empty board
print_board(board)

# Get the chosen square from the user
user_input = input("chose your square: ")

# If the square the user picked is empty, fill it with their symbol. Otherwise print that the square is already filled
if board[int(user_input) - 1] == ' ':
    board[int(user_input) - 1] = player_symbols[current_player]
else:
    print("slot already filled")

# Print the new board
print_board(board)
