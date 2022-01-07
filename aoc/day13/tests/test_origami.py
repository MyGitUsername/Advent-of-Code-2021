import unittest
import os
from ..file_processor import FileProcessor
from ..origami import Origami

class SimulationTestCase(unittest.TestCase):
    def setUp(self):
        fp = FileProcessor(os.path.dirname(__file__) + '/small-input.txt')
        self.origami = Origami(fp.dots(), fp.instructions())

    def test_transpose_up(self):
        new_pos = self.origami.transpose_up((0, 14), 7)
        self.assertEqual(new_pos, (0,0))

    def test_simulate_one_fold(self):
        self.origami.simulate(1)
        self.assertEqual(self.origami.number_of_dots(), 17)

    def test_simulate(self):
        self.origami.simulate()
        self.assertEqual(self.origami.number_of_dots(), 16)

    def test_transpose_vertical(self):
        new_pos = self.origami.transpose((0,1), 'x', 5)
        self.assertEqual((10, 1), new_pos)
