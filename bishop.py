from piece import Piece
from Position import Position



class Bishop(Piece):
    """Fou."""

    def isValidMove(self, newPosition: Position, board) -> bool:
        current = self.getPosition()
        if not self._canMoveTo(newPosition, board):
            return False

        col_delta = abs(Position.COLUMNS.index(current.getColumn()) - Position.COLUMNS.index(newPosition.getColumn()))
        row_delta = abs(current.getRow() - newPosition.getRow())

        return col_delta == row_delta and board.isPathClear(current, newPosition)

    def __str__(self) -> str:
        return "B"


if __name__ == "__main__":

    bishop = Bishop(Position("c", 1), 0)
    print("Pièce :", bishop)
    print("Position :", bishop.getPosition())
    print("Test Bishop OK !")
