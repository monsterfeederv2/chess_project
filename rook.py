from piece import Piece
from Position import Position


class Rook(Piece):
    """Tour."""

    def isValidMove(self, newPosition: Position, board) -> bool:
        current = self.getPosition()

        col_current = current.getColumn()
        row_current = current.getRow()

        col_new = newPosition.getColumn()
        row_new = newPosition.getRow()

        if not self._canMoveTo(newPosition, board):
            return False

        if col_current != col_new and row_current != row_new:
            return False

        return board.isPathClear(current, newPosition)

    def __str__(self) -> str:
        return "R"
