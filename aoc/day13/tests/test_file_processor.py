import unittest
import os
from ..file_processor import FileProcessor

class SimulationTestCase(unittest.TestCase):
    def setUp(self):
        self.file_processor = FileProcessor(os.path.dirname(__file__) + '/small-input.txt')

    def test_dots(self):
        actual = self.file_processor.dots()
        expected ={(6,10), (0,14), (9,10),
                   (0,3), (10,4), (4,11),
                   (6,0), (6,12), (4,1),
                   (0,13), (10,12), (3,4),
                   (3,0), (8,4), (1,10),
                   (2,14), (8,10), (9,0)}
        self.assertEqual(actual, expected)

    def test_instructions(self):
        actual = self.file_processor.instructions()
        expected =[('y', 7), ('x', 5)]
        self.assertEqual(actual, expected)
