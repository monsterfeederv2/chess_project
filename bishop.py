from piece import Piece
from Position import Position



class Bishop(Piece):
    """Fou."""

    def isValidMove(self, newPosition, board) -> bool:
        return True

    def __str__(self) -> str:
        return "B"


if __name__ == "__main__":

    bishop = Bishop(Position("c", 1), 0)
    print("Pièce :", bishop)
    print("Position :", bishop.getPosition())
    print("Test Bishop OK !")
