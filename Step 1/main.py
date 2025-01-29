# Save the board as a list of strings. When Empty they contain a space, Otherwise they are filled wit x or o
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# Use a function to print the board as we will need to do this many times
def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')

# For a function to run we need to call it. This will print out empty board
print_board(board)
