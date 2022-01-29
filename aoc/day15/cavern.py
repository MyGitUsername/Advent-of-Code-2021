from ..two_dimensional_array import TwoDimensionalArray
from ..cell import Cell

class Cavern(TwoDimensionalArray):
    def start(self) -> Cell:
        return self.get_cell(0, 0)

    def end(self) -> Cell:
        return self.get_cell(self.row_length() - 1, self.col_length() - 1)
        
