from Position import Position
from king import King
from queen import Queen
from bishop import Bishop
from knight import Knight
from rook import Rook
from pawn import Pawn


class Board:
    """Représente l'échiquier."""

    PIECE_TYPES = {
        "K": King,
        "Q": Queen,
        "B": Bishop,
        "N": Knight,
        "R": Rook,
        "P": Pawn,
    }

    def __init__(self):
        self.__pieces = []
        self.__initPieces()

    def __initPieces(self) -> None:
        # Pièces blanches
        self.__pieces.append(Rook(Position("a", 1), 0))
        self.__pieces.append(Knight(Position("b", 1), 0))
        self.__pieces.append(Bishop(Position("c", 1), 0))
        self.__pieces.append(Queen(Position("d", 1), 0))
        self.__pieces.append(King(Position("e", 1), 0))
        self.__pieces.append(Bishop(Position("f", 1), 0))
        self.__pieces.append(Knight(Position("g", 1), 0))
        self.__pieces.append(Rook(Position("h", 1), 0))

        for col in "abcdefgh":
            self.__pieces.append(Pawn(Position(col, 2), 0))

        # Pièces noires
        self.__pieces.append(Rook(Position("a", 8), 1))
        self.__pieces.append(Knight(Position("b", 8), 1))
        self.__pieces.append(Bishop(Position("c", 8), 1))
        self.__pieces.append(Queen(Position("d", 8), 1))
        self.__pieces.append(King(Position("e", 8), 1))
        self.__pieces.append(Bishop(Position("f", 8), 1))
        self.__pieces.append(Knight(Position("g", 8), 1))
        self.__pieces.append(Rook(Position("h", 8), 1))

        for col in "abcdefgh":
            self.__pieces.append(Pawn(Position(col, 7), 1))

    def getPosition(self, piece):
        for current_piece in self.__pieces:
            if current_piece == piece:
                return current_piece.getPosition()
        return None

    def getPiece(self, position: Position):
        for piece in self.__pieces:
            if piece.getPosition() == position:
                return piece
        return None

    def getPieces(self):
        return self.__pieces

    def clear(self) -> None:
        self.__pieces = []

    def addPiece(self, piece) -> None:
        self.__pieces.append(piece)

    def isPathClear(self, old_position: Position, new_position: Position) -> bool:
        old_col = old_position.getColumn()
        old_row = old_position.getRow()
        new_col = new_position.getColumn()
        new_row = new_position.getRow()

        col_step = 0
        row_step = 0

        if old_col != new_col:
            col_step = 1 if new_col > old_col else -1
        if old_row != new_row:
            row_step = 1 if new_row > old_row else -1

        columns = Position.COLUMNS
        col_index = columns.index(old_col)
        row = old_row

        while True:
            col_index += col_step
            row += row_step
            current = Position(columns[col_index], row)

            if current == new_position:
                return True

            if self.getPiece(current) is not None:
                return False

    def toData(self) -> list[dict]:
        data = []
        for piece in self.__pieces:
            data.append({
                "type": str(piece),
                "color": piece.getColor(),
                "position": piece.getPosition().getPosition(),
            })
        return data

    def loadData(self, pieces_data: list[dict]) -> None:
        self.clear()
        for item in pieces_data:
            piece_type = item["type"].upper()
            position_text = item["position"]
            position = Position(position_text[0], int(position_text[1]))
            piece_class = self.PIECE_TYPES[piece_type]
            self.addPiece(piece_class(position, int(item["color"])))

    def movePiece(self, old_position: Position, new_position: Position) -> bool:
        piece = self.getPiece(old_position)
        if piece is None:
            return False

        target = self.getPiece(new_position)

        if target is not None:
            if target.getColor() == piece.getColor():
                return False
            self.__pieces.remove(target)

        piece.setPosition(new_position)
        return True


if __name__ == "__main__":
    board = Board()
    print("Nombre de pièces :", len(board.getPieces()))
    print("Pièce en e1 :", board.getPiece(Position("e", 1)))
    print("Pièce en d8 :", board.getPiece(Position("d", 8)))
    print("Test Board OK !")
