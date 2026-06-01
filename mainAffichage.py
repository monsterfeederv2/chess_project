from chess import Chess
from Position import Position


def display_board_pretty(game):
    board = game.getBoard()

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

    while not game.isCheckMate():
        display_board_pretty(game)

        move = ""
        while not game.isValidMove(move):
            current_player = game.getCurrentPlayer()
            print(f"Au tour de {current_player.getName()}")
            move = current_player.askMove(board=game.getBoard()) if hasattr(current_player, "askMove") and current_player.__class__.__name__ == "AIPlayer" else current_player.askMove()

            if move.lower() == "save":
                game.saveGame()
                print("Partie sauvegardée.")
                move = ""
            elif move.lower() == "load":
                game.loadGame()
                print("Partie restaurée.")
                move = ""
            elif move.lower() == "quit":
                print("Partie terminée.")
                return

        game.updateBoard(move)
        game.switchPlayer()

    print(f"Échec et mat ! {game.getCurrentPlayer().getName()} a perdu.")


if __name__ == "__main__":
    main()
