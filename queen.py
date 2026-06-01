from piece import Piece
from Position import Position



class Queen(Piece):
    """Reine."""

    def isValidMove(self, newPosition: Position, board) -> bool:
        current = self.getPosition()
        if not self._canMoveTo(newPosition, board):
            return False

        col_delta = abs(Position.COLUMNS.index(current.getColumn()) - Position.COLUMNS.index(newPosition.getColumn()))
        row_delta = abs(current.getRow() - newPosition.getRow())
        is_straight = col_delta == 0 or row_delta == 0
        is_diagonal = col_delta == row_delta

        return (is_straight or is_diagonal) and board.isPathClear(current, newPosition)

    def __str__(self) -> str:
        return "Q"


if __name__ == "__main__":

    queen = Queen(Position("d", 1), 0)
    print("Pièce :", queen)
    print("Position :", queen.getPosition())
    print("Test Queen OK !")
