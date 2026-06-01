from piece import Piece
from Position import Position


class Pawn(Piece):
    """Pion."""

    def isValidMove(self, newPosition: Position, board) -> bool:
        current = self.getPosition()
        if not newPosition.isValid() or self._sameSquare(newPosition):
            return False

        direction = 1 if self.getColor() == 0 else -1
        start_row = 2 if self.getColor() == 0 else 7
        col_delta = Position.COLUMNS.index(newPosition.getColumn()) - Position.COLUMNS.index(current.getColumn())
        row_delta = newPosition.getRow() - current.getRow()
        target = board.getPiece(newPosition)

        if col_delta == 0:
            if target is not None:
                return False
            if row_delta == direction:
                return True
            if current.getRow() == start_row and row_delta == 2 * direction:
                middle = Position(current.getColumn(), current.getRow() + direction)
                return board.getPiece(middle) is None
            return False

        if abs(col_delta) == 1 and row_delta == direction:
            return target is not None and target.getColor() != self.getColor()

        return False

    def __str__(self) -> str:
        return "P"


if __name__ == "__main__":

    pawn = Pawn(Position("a", 2), 0)
    print("Pièce :", pawn)
    print("Position :", pawn.getPosition())
    print("Test Pawn OK !")
