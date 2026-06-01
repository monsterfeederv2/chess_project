import json

from board import Board
from player import Player
from aiplayer import AIPlayer
from Position import Position
from king import King


class Chess:
    """Gère globalement la partie d'échecs."""

    SAVE_FILE = "savegame.json"

    def __init__(self):
        self.__board = Board()
        self.__players = []
        self.__currentPlayer = None

    def __createPlayer(self, name: str, color: int) -> Player:
        if name.upper() == "AI":
            return AIPlayer(name, color)
        return Player(name, color)

    def initPlayers(self) -> None:
        names = []
        for i in range(2):
            names.append(input(f"Nom du joueur {i + 1} : "))

        self.setPlayers(names)

    def setPlayers(self, names: list[str]) -> None:
        if len(names) != 2:
            raise ValueError("Une partie d'échecs doit avoir exactement deux joueurs.")

        self.__players = []
        for color, name in enumerate(names):
            self.__players.append(self.__createPlayer(name, color))
        self.__currentPlayer = self.__players[0]

    def getBoard(self) -> Board:
        return self.__board

    def getCurrentPlayer(self) -> Player:
        return self.__currentPlayer

    def displayBoard(self) -> None:
        print("\n  a b c d e f g h")
        for row in range(8, 0, -1):
            line = str(row) + " "
            for col in "abcdefgh":
                piece = self.__board.getPiece(Position(col, row))
                if piece is None:
                    line += ". "
                else:
                    symbol = str(piece)
                    if piece.getColor() == 1:
                        symbol = symbol.lower()
                    line += symbol + " "
            print(line)
        print()

    def __parseMove(self, move: str):
        parts = move.split()
        if len(parts) != 2:
            return None

        old_pos_str, new_pos_str = parts

        expected_piece = None
        if len(old_pos_str) == 3:
            expected_piece = old_pos_str[0].upper()
            old_pos_str = old_pos_str[1:]

        if len(new_pos_str) == 3:
            if expected_piece is not None and new_pos_str[0].upper() != expected_piece:
                return None
            new_pos_str = new_pos_str[1:]

        if len(old_pos_str) != 2 or len(new_pos_str) != 2:
            return None

        try:
            old_position = Position(old_pos_str[0], int(old_pos_str[1]))
            new_position = Position(new_pos_str[0], int(new_pos_str[1]))
        except ValueError:
            return None

        if not old_position.isValid() or not new_position.isValid():
            return None

        return expected_piece, old_position, new_position

    def isValidMove(self, move: str) -> bool:
        parsed = self.__parseMove(move)
        if parsed is None:
            return False

        expected_piece, old_position, new_position = parsed

        piece = self.__board.getPiece(old_position)

        if piece is None:
            return False

        if expected_piece is not None and str(piece).upper() != expected_piece:
            return False

        if piece.getColor() != self.__currentPlayer.getColor():
            return False

        if not piece.isValidMove(new_position, self.__board):
            return False

        return not self.__wouldLeaveKingInCheck(piece, new_position)

    def __wouldLeaveKingInCheck(self, piece, new_position: Position) -> bool:
        old_position = piece.getPosition()
        captured_piece = self.__board.getPiece(new_position)

        if captured_piece is not None:
            self.__board.getPieces().remove(captured_piece)
        piece.setPosition(new_position)

        in_check = self.isInCheck(piece.getColor())

        piece.setPosition(old_position)
        if captured_piece is not None:
            self.__board.addPiece(captured_piece)

        return in_check

    def isInCheck(self, color: int) -> bool:
        king_position = None
        for piece in self.__board.getPieces():
            if isinstance(piece, King) and piece.getColor() == color:
                king_position = piece.getPosition()
                break

        if king_position is None:
            return True

        for piece in self.__board.getPieces():
            if piece.getColor() != color and piece.isValidMove(king_position, self.__board):
                return True

        return False

    def __hasLegalMove(self, color: int) -> bool:
        for piece in list(self.__board.getPieces()):
            if piece.getColor() != color:
                continue

            for column in Position.COLUMNS:
                for row in Position.ROWS:
                    destination = Position(column, row)
                    if piece.isValidMove(destination, self.__board):
                        if not self.__wouldLeaveKingInCheck(piece, destination):
                            return True

        return False

    def isCheckMate(self) -> bool:
        if self.__currentPlayer is None:
            return False
        color = self.__currentPlayer.getColor()
        return self.isInCheck(color) and not self.__hasLegalMove(color)

    def updateBoard(self, move: str) -> None:
        parsed = self.__parseMove(move)
        if parsed is None:
            return

        _, old_position, new_position = parsed
        self.__board.movePiece(old_position, new_position)

    def switchPlayer(self) -> None:
        if self.__currentPlayer == self.__players[0]:
            self.__currentPlayer = self.__players[1]
        else:
            self.__currentPlayer = self.__players[0]

    def __askCurrentPlayerMove(self) -> str:
        if isinstance(self.__currentPlayer, AIPlayer):
            return self.__currentPlayer.askMove(self.__board)
        return self.__currentPlayer.askMove()

    def __handleCommand(self, move: str) -> bool:
        command = move.lower()

        if command == "save":
            self.saveGame()
            print("Partie sauvegardée.")
            return True

        if command == "load":
            self.loadGame()
            print("Partie restaurée.")
            return True

        if command == "quit":
            print("Partie terminée.")
            return True

        return False

    def saveGame(self, filename: str = SAVE_FILE) -> None:
        data = {
            "current_player_color": self.__currentPlayer.getColor(),
            "players": [
                {"name": player.getName(), "color": player.getColor(), "type": player.__class__.__name__}
                for player in self.__players
            ],
            "pieces": self.__board.toData(),
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def loadGame(self, filename: str = SAVE_FILE) -> None:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.__players = []
        for item in data["players"]:
            player_class = AIPlayer if item["type"] == "AIPlayer" else Player
            self.__players.append(player_class(item["name"], item["color"]))

        self.__board.loadData(data["pieces"])
        current_color = data["current_player_color"]
        self.__currentPlayer = next(player for player in self.__players if player.getColor() == current_color)

    def play(self, display_function=None) -> None:
        self.initPlayers()

        while not self.isCheckMate():
            if display_function is None:
                self.displayBoard()
            else:
                display_function(self)

            move = ""
            while not self.isValidMove(move):
                print(f"Au tour de {self.__currentPlayer.getName()}")
                move = self.__askCurrentPlayerMove()

                if self.__handleCommand(move):
                    if move.lower() == "quit":
                        return
                    move = ""

            self.updateBoard(move)
            self.switchPlayer()

        print(f"Échec et mat ! {self.__currentPlayer.getName()} a perdu.")


if __name__ == "__main__":
    game = Chess()
    print("Classe Chess créée avec succès.")
    print("Lance game.play() pour commencer une partie.")
