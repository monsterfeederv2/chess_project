from piece import Piece
from  Position import Position


class King(Piece):
    """Roi."""

    def isValidMove(self, newPosition, board) -> bool:
        return True

    def __str__(self) -> str:
        return "K"


if __name__ == "__main__":

    king = King(Position("e", 1), 0)
    print("Pièce :", king)
    print("Position :", king.getPosition())
    print("Test King OK !")
