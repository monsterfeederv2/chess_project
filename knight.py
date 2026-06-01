from piece import Piece
from Position import Position

class Knight(Piece):
    """Cavalier."""

    def isValidMove(self, newPosition: Position, board) -> bool:
        current = self.getPosition()
        if not self._canMoveTo(newPosition, board):
            return False

        col_delta = abs(Position.COLUMNS.index(current.getColumn()) - Position.COLUMNS.index(newPosition.getColumn()))
        row_delta = abs(current.getRow() - newPosition.getRow())

        return (col_delta, row_delta) in [(1, 2), (2, 1)]

    def __str__(self) -> str:
        return "N"


if __name__ == "__main__":

    knight = Knight(Position("b", 1), 0)
    print("Pièce :", knight)
    print("Position :", knight.getPosition())
    print("Test Knight OK !")
      
