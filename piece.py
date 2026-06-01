from abc import ABC, abstractmethod
from Position import Position


class Piece(ABC):
    """Classe abstraite représentant une pièce d'échecs."""

    def __init__(self, position: Position, color: int):
        self.__position = position
        self.__color = color  # 0 = blanc, 1 = noir

    def getPosition(self) -> Position:
        return self.__position

    def setPosition(self, new_position: Position) -> None:
        self.__position = new_position

    def getColor(self) -> int:
        return self.__color

    def _sameSquare(self, newPosition: Position) -> bool:
        return self.__position == newPosition

    def _canMoveTo(self, newPosition: Position, board) -> bool:
        if not newPosition.isValid() or self._sameSquare(newPosition):
            return False

        target = board.getPiece(newPosition)
        return target is None or target.getColor() != self.__color

    @abstractmethod
    def isValidMove(self, newPosition: Position, board) -> bool:
        """Retourne True si le déplacement est valide."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


if __name__ == "__main__":
    print("La classe Piece est abstraite, on la teste via ses sous-classes.")
