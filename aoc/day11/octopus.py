from ..cell import Cell

class Octopus(Cell):
    def __init__(self, row_idx, col_idx, energy):
        super().__init__(row_idx, col_idx, energy)
        self.flashed_this_turn = False

    @property
    def value(self):
        return super().value

    @value.setter
    def value(self, new_value):
        return super(Octopus, type(self)).value.fset(self, new_value)

    def step1(self):
        self.value += 1

    def step2(self, get_adjacent_octopus):
        if self.value > 9 and not self.flashed_this_turn:
            self.flashed_this_turn = True
            for adjacent_octopus in get_adjacent_octopus(self):
                adjacent_octopus.value += 1
                if adjacent_octopus.value > 9:
                    adjacent_octopus.step2(get_adjacent_octopus)

    def step3(self):
        if self.flashed_this_turn:
            self.value = 0
            self.flashed_this_turn = False
            return True
        return False
