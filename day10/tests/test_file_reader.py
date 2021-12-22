import unittest

import os
import sys
sys.path.append(os.path.abspath('..'))

from file_reader import FileReader

class SimulationTestCase(unittest.TestCase):
    def setUp(self):
        self.file_reader = FileReader('test-input-small.txt')

    def test_file_reader(self):
        actual = self.file_reader.process_file()
        expected = [['[','(', '{', '('],
                    [ '[', '(', '(', ')'],
                    ['{', '(', '[', '(']] 
        self.assertEqual(actual, expected)
