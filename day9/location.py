from functools import total_ordering

@total_ordering
class Location:
    def __init__(self, row_idx, col_idx, height): 
        self._row_idx = row_idx
        self._col_idx = col_idx
        self._height = height

    @property
    def row_idx(self):
        return self._row_idx

    @property
    def col_idx(self):
        return self._col_idx

    @property
    def height(self):
        return self._height

    def __hash__(self):
        return hash((self.row_idx, self.col_idx, self.height))

    def __eq__(self, o):
        if isinstance(o, Location):
            return self.row_idx == o.row_idx and self.col_idx == o.col_idx and self.height == o.height
        return False

    def __gt__(self, o):
        return self.height > o.height

    def __repr__(self):
        return str(self.height)
