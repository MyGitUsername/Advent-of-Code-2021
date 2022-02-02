from ..two_dimensional_array import TwoDimensionalArray
from ..cell import Cell
import numpy as np
from typing import List

class Cavern(TwoDimensionalArray):
    def start(self) -> Cell:
        return self.get_cell(0, 0)

    def end(self) -> Cell:
        return self.get_cell(self.row_length() - 1, self.col_length() - 1)

    def transpose_tile(self, original_tile, rel_pos):
        return [[Cavern.increase_risk_lvl(risk_lvl, rel_pos) 
                for risk_lvl in row] for row in original_tile] 

    def determine_call_val(self, cell, rel_pos):
        cell_val = cell.value + rel_pos
        if cell_val > 9:
            cell_val = cell_val % 9
        return cell_val
    
    def generate_tiles(self):
        return [self.transpose_tile(self.risk_levels(), relative_pos) for relative_pos in range(1, 9)]

    def gen_large_cavern(self):
        tiles = self.generate_tiles()
        row1 = np.concatenate((self.risk_levels(), tiles[0], tiles[1], tiles[2], tiles[3]), axis=1)
        row2 =  np.concatenate((tiles[0], tiles[1], tiles[2], tiles[3], tiles[4]), axis=1)
        row3 = np.concatenate((tiles[1], tiles[2], tiles[3], tiles[4], tiles[5]), axis=1)
        row4 = np.concatenate((tiles[2], tiles[3], tiles[4], tiles[5], tiles[6]), axis=1)
        row5 = np.concatenate((tiles[3], tiles[4], tiles[5], tiles[6], tiles[7]), axis=1)
        full_map = np.concatenate((row1, row2, row3,row4, row5))

        return self.make_cells(full_map)

    def make_cells(self, proto):
        cavern = []
        for i, row in enumerate(proto):
            new_row = []
            for j, value in enumerate(row):
                new_row.append(Cell(i, j, value))
            cavern.append(new_row)
        return Cavern(cavern)

    def risk_levels(self) -> List[List[int]]:
        return [[cell.value for cell in row] for row in self.two_dimensional_array]

    @classmethod
    def increase_risk_lvl(cls, risk_lvl, rel_pos) -> int:
        inc_risk_lvl = risk_lvl + rel_pos
        return inc_risk_lvl % 9 if inc_risk_lvl > 9 else inc_risk_lvl
