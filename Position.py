class Position:
    """Représente une position sur l'échiquier, par exemple e4."""

    def __init__(self, column: str, row: int):
        self.__column = column
        self.__row = row

    def getColumn(self) -> str:
        return self.__column

    def getRow(self) -> int:
        return self.__row

    def getPosition(self) -> str:
        return f"{self.__column}{self.__row}"

    def __str__(self) -> str:
        return self.getPosition()

    def __eq__(self, other) -> bool:
        if not isinstance(other, Position):
            return False
        return self.__column == other.__column and self.__row == other.__row


if __name__ == "__main__":
    p1 = Position("e", 4)
    p2 = Position("a", 1)

    print("Position 1 :", p1)   # e4
    print("Position 2 :", p2)   # a1
    print("Tests Position OK !")
