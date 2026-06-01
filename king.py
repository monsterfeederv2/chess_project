from piece import Piece
from Position import Position


class King(Piece):
    """Roi."""

    def isValidMove(self, newPosition: Position, board) -> bool:
        current = self.getPosition()
        if not self._canMoveTo(newPosition, board):
            return False

        col_delta = abs(Position.COLUMNS.index(current.getColumn()) - Position.COLUMNS.index(newPosition.getColumn()))
        row_delta = abs(current.getRow() - newPosition.getRow())

        return col_delta <= 1 and row_delta <= 1

    def __str__(self) -> str:
        return "K"


if __name__ == "__main__":

    king = King(Position("e", 1), 0)
    print("Pièce :", king)
    print("Position :", king.getPosition())
    print("Test King OK !")
