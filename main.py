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

user_input = input("chose your square: ")

if board[int(user_input) - 1] == ' ':
    board[int(user_input) - 1] = player_symbols[current_player]
else:
    print("slot already filled")

print_board(board)
