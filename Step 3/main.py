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
# We implement a while loop to continue the game
while True:
    user_input = input("chose your square: ")

    if board[int(user_input) - 1] == ' ':
        board[int(user_input) - 1] = player_symbols[current_player]
    else:
        print("slot already filled")
        # The continue statement skips the rest of the code and goes back to the start of the loop.
        # This is because if the slot is fulled we don't want to switch whose turn it is next as their input was invalid
        continue

    if current_player == 0:
        current_player = 1
    elif current_player == 1:
        current_player = 0
    print_board(board)
