import functools

# Cells:
#
# [14, 21, 17, 24,  4,
#  10, 16, 15,  9, 19,
#  18,  8, 23, 26, 20,
#  22, 11, 13,  6,  5,
#  2, 0, 12,  3,  7]

class BingoBoard:
    def __init__(self, cells):
        self._cells = cells;
        self._bingo = []
        self._winner = False

    @property
    def cells(self):
        return self._cells

    @property
    def winner(self):
        return self._winner

    @property
    def bingo(self):
        return self._bingo

    # replace number with 'X'
    def mark_cell(self, n):
        for i in range(len(self.cells)): 
            if self.cells[i] == n:
                self.cells[i] = 'X'
        if self.is_bingo():
            self._winner = True

    
    def is_cell_marked(self, index):
        return True if self.cells[index] == 'X' else False

    def get_number(self, i):
        return self.cells[i]

    def is_bingo_row(self):
        run = []
        row_len = 5

        for i in range(0, len(self.cells), row_len):
            last_cell_in_sequence = i + 4
            for j in range(i, i + row_len):
                run.append(self.get_number(j))
                if not self.is_cell_marked(j):
                    break
                elif j == last_cell_in_sequence: 
                    self._bingo = run
                    return True
        return False

    def is_bingo_column(self):
        run = []
        col_len = 5
        row_len = 5

        for i in range(0, row_len):
            last_cell_in_sequence = i + 20
            for j in range(i, len(self.cells), col_len):
                run.append(self.get_number(j))
                if not self.is_cell_marked(j):
                    break
                elif j == last_cell_in_sequence:
                    self._bingo = run
                    return True
        return False

    def is_bingo_diagonal(self):
        # cells index: 0, 6, 12, 18, 24
        if (self.is_cell_marked(0) and 
                self.is_cell_marked(6) and 
                self.is_cell_marked(12) and 
                self.is_cell_marked(18) and 
                self.is_cell_marked(24)): 
            self._bingo = [self.get_number(0), 
                          self.get_number(6), 
                          self.get_number(12), 
                          self.get_number(18), 
                          self.get_number(24)]
            return True
        # cells index: 4, 8, 12, 16, 20
        elif (self.is_cell_marked(4) and 
                self.is_cell_marked(8) and 
                self.is_cell_marked(12) and 
                self.is_cell_marked(16) and 
                self.is_cell_marked(20)): 
            self._bingo = [self.get_number(4), 
                          self.get_number(8), 
                          self.get_number(12), 
                          self.get_number(16), 
                          self.get_number(20)]
            return True
        else: 
            return False

    def is_bingo(self):
        if self.is_bingo_column() or self.is_bingo_row():
            return True
        return False

    def calculate_score(self, last_number_called):
        unmarked_cells = list(filter(lambda cell: cell != 'X', self.cells))
        sum_of_unmarked = functools.reduce(lambda x, y: x + y, unmarked_cells)

        return last_number_called * sum_of_unmarked


