import unittest

from ...file_reader import FileReader
from ...two_dimensional_array import TwoDimensionalArray
from ..simulation import Simulation
from ..octopus import Octopus

class SimulationTestCase(unittest.TestCase):
    def setUp(self):
        self.file_reader = FileReader('test-input.txt')

    def test_one_step(self):
        input = FileReader('AoC/day11/tests/small-input/before-any-steps.txt').process_file(Octopus)
        sim = Simulation(TwoDimensionalArray(input), 1)
        sim.run_steps()
        result = FileReader('small-input/after-one-step.txt').process_file(Octopus)
        self.assertEqual(sim.board, result)
