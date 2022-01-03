import unittest

from ..file_reader import GraphFileReader
from ..path import Path
import pdb
import os

class SimulationTestCase(unittest.TestCase):
    def setUp(self):
        self.file_reader = GraphFileReader(os.path.dirname(__file__) + '/small-input.txt')

    def test_sample(self):
        edges = self.file_reader.process_file()
        path_finder = Path(edges)
        path_finder.find_paths()
        pdb.set_trace()
        self.assertEqual(10, len(path_finder.paths))
