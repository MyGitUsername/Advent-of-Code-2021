import unittest

import os
import sys
sys.path.append(os.path.abspath('..'))

from file_reader import FileReader

class SimulationTestCase(unittest.TestCase):
    def setUp(self):
        self.file_reader = FileReader('test-input.txt')

    def test_find_best_pos(self):
        actual = self.file_reader.process_file()
        expected = [[2,1,9,9,9,4,3,2,1,0],
                    [3,9,8,7,8,9,4,9,2,1],
                    [9,8,5,6,7,8,9,8,9,2],
                    [8,7,6,7,8,9,6,7,8,9],
                    [9,8,9,9,9,6,5,6,7,8]]
        self.assertEqual(actual, expected)
