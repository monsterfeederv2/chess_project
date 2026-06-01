from chess import Chess
from Position import Position


def display_board_pretty(game):
    board = game.getBoard()

    symbols = {
        (0, "K"): "♔", (0, "Q"): "♕", (0, "R"): "♖",
        (0, "B"): "♗", (0, "N"): "♘", (0, "P"): "♙",
        (1, "K"): "♚", (1, "Q"): "♛", (1, "R"): "♜",
        (1, "B"): "♝", (1, "N"): "♞", (1, "P"): "♟",
    }

    print("\n   a  b  c  d  e  f  g  h")
    for row in range(8, 0, -1):
        line = str(row) + " "
        for col in "abcdefgh":
            piece = board.getPiece(Position(col, row))

            if piece is None:
                line += " . "
            else:
                symbol = symbols.get((piece.getColor(), str(piece).upper()), "?")
                line += f" {symbol} "
        print(line)
    print()


def main():
    game = Chess()
    game.play(display_board_pretty)


if __name__ == "__main__":
    main()
