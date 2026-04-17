from piece import Piece
from Position import Position



class Queen(Piece):
    """Reine."""

    def isValidMove(self, newPosition, board) -> bool:
        return True

    def __str__(self) -> str:
        return "Q"


if __name__ == "__main__":

    queen = Queen(Position("d", 1), 0)
    print("Pièce :", queen)
    print("Position :", queen.getPosition())
    print("Test Queen OK !")
