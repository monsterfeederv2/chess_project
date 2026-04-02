import random
from player import Player


class AIPlayer(Player):
    """Joueur IA très simple."""

    def askMove(self) -> str:
        columns = "abcdefgh"
        start_col = random.choice(columns)
        end_col = random.choice(columns)
        start_row = random.randint(1, 8)
        end_row = random.randint(1, 8)

        return f"{start_col}{start_row} {end_col}{end_row}"


if __name__ == "__main__":
    ai = AIPlayer("AI", 1)
    print("Coup généré :", ai.askMove())
    print("Test AIPlayer OK !")
