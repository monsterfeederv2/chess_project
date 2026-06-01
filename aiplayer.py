import random
from player import Player
from Position import Position


class AIPlayer(Player):
    """Joueur IA très simple."""

    def askMove(self, board=None) -> str:
        if board is not None:
            possible_moves = []
            for piece in board.getPieces():
                if piece.getColor() != self.getColor():
                    continue
                for column in Position.COLUMNS:
                    for row in Position.ROWS:
                        destination = Position(column, row)
                        if piece.isValidMove(destination, board):
                            possible_moves.append(
                                f"{piece}{piece.getPosition()} {piece}{destination}"
                            )

            if possible_moves:
                move = random.choice(possible_moves)
                print(f"{self.getName()} joue : {move}")
                return move

        piece = random.choice("KQBNRP")
        columns = Position.COLUMNS
        start_col = random.choice(columns)
        end_col = random.choice(columns)
        start_row = random.choice(list(Position.ROWS))
        end_row = random.choice(list(Position.ROWS))

        return f"{piece}{start_col}{start_row} {piece}{end_col}{end_row}"


if __name__ == "__main__":
    ai = AIPlayer("AI", 1)
    print("Coup généré :", ai.askMove())
    print("Test AIPlayer OK !")
