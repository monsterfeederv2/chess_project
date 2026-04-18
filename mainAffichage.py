from chess import Chess
from Position import Position


def display_board_pretty(game):
    # accès au board (hack nécessaire sans modifier Chess)
    board = game._Chess__board

    symbols = {
        "K": "♔", "Q": "♕", "R": "♖",
        "B": "♗", "N": "♘", "P": "♙"
    }

    print("\n   a  b  c  d  e  f  g  h")
    for row in range(8, 0, -1):
        line = str(row) + " "
        for col in "abcdefgh":
            piece = board.getPiece(Position(col, row))

            if piece is None:
                line += " . "
            else:
                symbol = symbols.get(str(piece).upper(), "?")

                # pièces noires en minuscule
                if piece.getColor() == 1:
                    symbol = symbol.lower()

                line += f" {symbol} "
        print(line)
    print()


def main():
    game = Chess()
    game.initPlayers()

    while True:
        display_board_pretty(game)

        move = ""
        while not game.isValidMove(move):
            print(f"Au tour de {game._Chess__currentPlayer.getName()}")
            move = game._Chess__currentPlayer.askMove()

        game.updateBoard(move)
        game.switchPlayer()


if __name__ == "__main__":
    main()