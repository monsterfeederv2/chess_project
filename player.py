class Player:
    """Représente un joueur humain."""

    def __init__(self, name: str, color: int):
        self.__name = name
        self.__color = color

    def getName(self) -> str:
        return self.__name

    def getColor(self) -> int:
        return self.__color

    def askMove(self) -> str:
        return input(f"{self.__name}, entrez votre coup : ")

    def __str__(self) -> str:
        return self.__name


if __name__ == "__main__":
    player = Player("Hugo", 0)
    print("Joueur :", player)
    print("Couleur :", player.getColor())
    print("Test Player OK !")
