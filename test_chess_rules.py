import os
import tempfile
import unittest

from Position import Position
from board import Board
from chess import Chess


class TestChessRules(unittest.TestCase):
    def test_initial_board_contains_32_pieces(self):
        board = Board()
        self.assertEqual(len(board.getPieces()), 32)
        self.assertEqual(str(board.getPiece(Position("e", 1))), "K")
        self.assertEqual(str(board.getPiece(Position("d", 8))), "Q")

    def test_rook_cannot_jump_over_piece(self):
        board = Board()
        rook = board.getPiece(Position("a", 1))
        self.assertFalse(rook.isValidMove(Position("a", 4), board))

    def test_knight_can_jump(self):
        board = Board()
        knight = board.getPiece(Position("b", 1))
        self.assertTrue(knight.isValidMove(Position("c", 3), board))

    def test_pawn_moves_and_captures(self):
        board = Board()
        white_pawn = board.getPiece(Position("e", 2))
        self.assertTrue(white_pawn.isValidMove(Position("e", 4), board))
        self.assertFalse(white_pawn.isValidMove(Position("e", 5), board))

        board.movePiece(Position("d", 7), Position("d", 3))
        self.assertTrue(white_pawn.isValidMove(Position("d", 3), board))

    def test_chess_accepts_subject_move_format(self):
        game = Chess()
        game.setPlayers(["Blanc", "Noir"])
        self.assertTrue(game.isValidMove("Nb1 Nc3"))
        self.assertFalse(game.isValidMove("Rb1 Rc3"))

    def test_save_and_load_game(self):
        game = Chess()
        game.setPlayers(["Blanc", "Noir"])
        game.updateBoard("Pe2 Pe4")

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            filename = temp_file.name

        try:
            game.saveGame(filename)

            restored = Chess()
            restored.loadGame(filename)

            self.assertIsNone(restored.getBoard().getPiece(Position("e", 2)))
            self.assertEqual(str(restored.getBoard().getPiece(Position("e", 4))), "P")
            self.assertEqual(restored.getCurrentPlayer().getName(), "Blanc")
        finally:
            os.remove(filename)


if __name__ == "__main__":
    unittest.main()
