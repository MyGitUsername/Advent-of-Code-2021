import unittest
import os
import sys
sys.path.append(os.path.abspath('..'))

from file_reader import FileReader
from lava_tubes import LavaTubes

class SimulationTestCase(unittest.TestCase):
    def setUp(self):
        self.file_reader = FileReader('test-input.txt')

    def test_find_low_points(self):
        heat_map = self.file_reader.process_file()
        lt = LavaTubes(heat_map)
        lt.find_low_points()
        self.assertEqual(lt.sum_of_risk_lvl(), 15)

    def test_answer_part_2(self):
        heat_map = self.file_reader.process_file()
        lt = LavaTubes(heat_map)
        lt.find_low_points()
        lt.find_basins()
        self.assertEqual(lt.result_part_two(), 1134)
