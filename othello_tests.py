def legal_move(game_board: list[list[int]], player: int, coordinates: tuple[int, int]) -> bool: pass

import unittest

class TestLegalMove(unittest.TestCase):
    def test_legal_move_legal_up(self) -> None:
        board = [[0,0,0,0],
                 [0,0,0,0],
                 [0,2,0,0],
                 [0,1,0,0]]
        self.assertTrue(legal_move(board, 1, (1, 1)))

    def test_legal_move_legal_dur(self) -> None:
        board = [[0,0,0,0],
                 [0,0,1,0],
                 [0,1,0,0],
                 [2,0,0,0]]
        self.assertTrue(legal_move(board, 2, (3, 0)))

    def test_legal_move_legal_right(self) -> None:
        board = [[0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0],
                 [1,2,2,0]]
        self.assertTrue(legal_move(board, 1, (3, 3)))

    def test_legal_move_illegal_occupied(self) -> None:
        board = [[0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0],
                 [1,2,2,1]]
        self.assertFalse(legal_move(board, 1, (3, 3)))

    def test_legal_move_illegal_gap(self) -> None:
        board = [[0,0,0,0],
                 [0,0,1,2],
                 [0,0,0,0],
                 [0,0,0,0]]
        self.assertFalse(legal_move(board, 2, (0, 1)))

    def test_legal_move_bad_values(self) -> None:
        board = [[0,0,0,0],
                 [0,0,1,2],
                 [0,0,3,0],
                 [0,0,0,0]]
        with self.assertRaises(ValueError):
            legal_move(board, 1, (2, 1))

    def test_legal_move_bad_size(self) -> None:
        board = [[0,0,0,0],
                 [0,0,1,2],
                 [0,0,1,0,1],
                 [0,0,0,0]]
        with self.assertRaises(ValueError):
            legal_move(board, 2, (1, 1))

    def test_legal_move_bad_coordinates(self) -> None:
        board = [[0,0,0,0],
                 [0,0,1,2],
                 [0,0,1,0],
                 [0,0,0,0]]
        with self.assertRaises(ValueError):
            legal_move(board, 1, (4, 0))


if __name__ == "__main__":
    unittest.main()