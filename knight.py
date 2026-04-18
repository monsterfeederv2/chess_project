from piece import Piece
from Position import Position

class Knight(Piece):
    """Cavalier."""

    def isValidMove(self, newPosition, board) -> bool:
        return True

    def __str__(self) -> str:
        return "N"


if __name__ == "__main__":

    knight = Knight(Position("b", 1), 0)
    print("Pièce :", knight)
    print("Position :", knight.getPosition())
    print("Test Knight OK !")
      
