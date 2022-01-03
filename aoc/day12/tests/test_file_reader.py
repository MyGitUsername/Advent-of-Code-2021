import unittest

from ..file_reader import GraphFileReader

class SimulationTestCase(unittest.TestCase):
    def setUp(self):
        self.file_reader = GraphFileReader('AoC/day12/tests/small-input.txt')

    def test_file_reader(self):
        actual = self.file_reader.process_file()
        expected = [('start', 'A'),
                    ('start', 'b'),
                    ('A', 'c'),
                    ('A', 'b'),
                    ('b', 'd'),
                    ('A', 'end'),
                    ('b', 'end')]
        self.assertEqual(actual, expected)
