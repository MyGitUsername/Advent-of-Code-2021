import unittest
import os
from ..file_processor import FileProcessor
from ..run import Run
import pdb

class RunTestCase(unittest.TestCase):
    def setUp(self):
        self.fp = FileProcessor(os.path.dirname(__file__) + '/small-input.txt')
        self.run = Run(self.fp.polymer_template(), self.fp.pair_insertion_rules())

    def test_run_one_step(self):
        pdb.set_trace()
        self.run.run(1)
        self.assertEqual(self.run.final_polymer, 'NCNBCHB')

    def test_run_two_steps(self):
        self.run.run(2)
        self.assertEqual(self.run.final_polymer, 'NBCCNBBBCBHCB')

    def test_run_three_steps(self):
        self.run.run(3)
        self.assertEqual(self.run.final_polymer, 'NBBBCNCCNBBNBNBBCHBHHBCHB')

    def test_run_four_steps(self):
        self.run.run(4)
        self.assertEqual(self.run.final_polymer, 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')

    def test_result(self):
        self.run.run(10)
        res = self.run.get_result()
        self.assertEqual(res, 1588)

