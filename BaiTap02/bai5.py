import chess

def fen_to_board(fen):
    board = chess.Board(fen)
    return board

fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
board = fen_to_board(fen)
print(board)