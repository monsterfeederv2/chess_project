from piece import Piece
from Position import Position


class Pawn(Piece):
    """Pion."""

    def isValidMove(self, newPosition, board) -> bool:
        return True

    def __str__(self) -> str:
        return "P"


if __name__ == "__main__":

    pawn = Pawn(Position("a", 2), 0)
    print("Pièce :", pawn)
    print("Position :", pawn.getPosition())
    print("Test Pawn OK !")
