from ..file_reader import FileReader
from ..two_dimensional_array import TwoDimensionalArray
from .octopus import Octopus

class Simulation:
    def __init__(self, board, steps):
        self._board = board
        self._steps = steps
        self._total_flashes = 0
        self._first_simultaneous_flash = 0

    @property
    def steps(self):
        return self._steps

    @property
    def total_flashes(self):
        return self._total_flashes

    @property
    def first_simultaneous_flash(self):
        return self._first_simultaneous_flash

    @property
    def board(self):
        return self._board

    @total_flashes.setter
    def total_flashes(self, total_flashes):
        self._total_flashes= total_flashes   

    @first_simultaneous_flash.setter
    def first_simultaneous_flash(self, first_simultaneous_flash):
        self._first_simultaneous_flash = first_simultaneous_flash   

    def octopuses(self):
        return self.board.flatten()
    
    def is_simultaneous_flash(self, num_flashed_this_step):
        return True if num_flashed_this_step == len(self.octopuses()) else False

    def run_step(self, step):
        for ocotopus in self.octopuses():
            ocotopus.step1()

        for ocotopus in self.octopuses():
            ocotopus.step2(self.board.get_all_surounding_locs)

        num_flashed_this_step = 0
        for ocotopus in self.octopuses():
            flashed = ocotopus.step3()
            if flashed:
                self.total_flashes += 1
                num_flashed_this_step += 1

        if self.is_simultaneous_flash(num_flashed_this_step) and self.first_simultaneous_flash == 0:
            self.first_simultaneous_flash = step + 1

    def run_steps(self):
        for i in range(self.steps):
            self.run_step(i)

if __name__ == "__main__":
    input = FileReader('AoC/day11/input.txt').process_file(Octopus)
    board = TwoDimensionalArray(input)
    sim = Simulation(TwoDimensionalArray(input), 1000)
    sim.run_steps()
    print(f'num of flashes: {sim.total_flashes}')
    print(f'first_simultaneous_flash: {sim.first_simultaneous_flash}')

