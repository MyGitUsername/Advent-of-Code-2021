from functools import total_ordering

@total_ordering
class Cell:
    def __init__(self, row_idx, col_idx, value): 
        self._row_idx = row_idx
        self._col_idx = col_idx
        self._value = value

    @property
    def row_idx(self):
        return self._row_idx

    @property
    def col_idx(self):
        return self._col_idx

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __hash__(self):
        return hash((self.row_idx, self.col_idx, self.value))

    def __eq__(self, o):
        if isinstance(o, Cell):
            return self.row_idx == o.row_idx and self.col_idx == o.col_idx and self.value == o.value
        return False

    def __gt__(self, o):
        return self.value > o.value

    def __repr__(self):
        return str(self.value)
