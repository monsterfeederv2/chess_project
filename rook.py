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

        # ✅ La tour doit rester sur la même ligne ou colonne
        if col_current != col_new and row_current != row_new:
            return False

        # 🔍 Vérifier les obstacles

        # Cas vertical
        if col_current == col_new:
            step = 1 if row_new > row_current else -1

            for r in range(row_current + step, row_new, step):
                if board.getPiece(Position(col_current, r)) is not None:
                    return False

        # Cas horizontal
        elif row_current == row_new:
            cols = "abcdefgh"

            start = cols.index(col_current)
            end = cols.index(col_new)

            step = 1 if end > start else -1

            for i in range(start + step, end, step):
                if board.getPiece(Position(cols[i], row_current)) is not None:
                    return False

        return True

    def __str__(self) -> str:
        return "R"