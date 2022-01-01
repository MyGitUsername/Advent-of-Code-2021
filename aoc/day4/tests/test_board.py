import unittest

# FIXME: improved relative imports python
import os
import sys
sys.path.append(os.path.abspath('..'))

from bingo_board import BingoBoard


class BoardTestCase(unittest.TestCase):
    def setUp(self):
        self.board = BingoBoard([14, 21, 17, 24,  4,
                                 10, 16, 15,  9, 19,
                                 18,  8, 23, 26, 20,
                                 22, 11, 13,  6,  5,
                                 2, 0, 12,  3,  7])
    
    def test_mark_cell(self):
        self.board.mark_cell(14)
        self.assertEqual(self.board.cells[0], 'X')

    def test_mark_another_cell(self):
        self.board.mark_cell(23)
        self.assertEqual(self.board.cells[12], 'X')

    def test_premature_bingo(self):
        self.board.mark_cell(14)
        self.board.mark_cell(21)
        self.board.mark_cell(17)
        self.board.mark_cell(24)
        self.assertEqual(self.board.is_bingo(), False)

    def test_bingo_first_row(self):
        self.board.mark_cell(14)
        self.board.mark_cell(21)
        self.board.mark_cell(17)
        self.board.mark_cell(24)
        self.board.mark_cell(4)
        self.assertEqual(self.board.is_bingo(), True)

    def test_bingo_last_row(self):
        self.board.mark_cell(2)
        self.board.mark_cell(0)
        self.board.mark_cell(12)
        self.board.mark_cell(3)
        self.board.mark_cell(7)
        self.assertEqual(self.board.is_bingo(), True)

    def test_bingo_first_col(self):
        self.board.mark_cell(14)
        self.board.mark_cell(10)
        self.board.mark_cell(18)
        self.board.mark_cell(22)
        self.board.mark_cell(2)
        self.assertEqual(self.board.is_bingo(), True)

    def test_premature_bingo_last_column(self):
        self.board.mark_cell(4)
        self.board.mark_cell(19)
        self.board.mark_cell(20)
        self.board.mark_cell(5)
        self.assertEqual(self.board.is_bingo(), False)

    def test_another_premature_bingo_last_column(self):
        self.board.mark_cell(4)
        self.board.mark_cell(19)
        self.board.mark_cell(20)
        self.board.mark_cell(7)
        self.assertEqual(self.board.is_bingo(), False)

    def test_bingo_last_column(self):
        self.board.mark_cell(5)
        self.board.mark_cell(4)
        self.board.mark_cell(19)
        self.board.mark_cell(20)
        self.board.mark_cell(7)
        self.assertEqual(self.board.is_bingo(), True)

    # def test_diagonal_bingo_left_to_right(self):
    #     self.board.mark_cell(14)
    #     self.board.mark_cell(16)
    #     self.board.mark_cell(23)
    #     self.board.mark_cell(6)
    #     self.board.mark_cell(7)
    #     self.assertEqual(self.board.is_bingo(), True)

    # def test_diagonal_bingo_right_to_left(self):
    #     self.board.mark_cell(4)
    #     self.board.mark_cell(9)
    #     self.board.mark_cell(23)
    #     self.board.mark_cell(11)
    #     self.board.mark_cell(2)
    #     self.assertEqual(self.board.is_bingo(), True)

    def test_calculate_score(self):
        self.board.mark_cell(14)
        self.board.mark_cell(16)
        self.board.mark_cell(23)
        self.board.mark_cell(6)
        self.board.mark_cell(7)
        self.assertEqual(self.board.calculate_score(7), 1813)
