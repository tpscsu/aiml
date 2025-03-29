chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],  # Black pieces
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],  # Black pawns
    ['.', '.', '.', '.', '.', '.', '.', '.'],  # Empty rows
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  # White pawns
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']  # White pieces
]


def print_chess_board(board):
    for row in board:
        print(' '.join(row))
    print()


print_chess_board(chess_board)

chess_board[4][4] = chess_board[6][4]  # Move pawn to e4
chess_board[6][4] = '.'  # e2 is now empty

print_chess_board(chess_board)
