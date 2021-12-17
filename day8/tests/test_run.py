import unittest
import os
import sys
sys.path.append(os.path.abspath('..'))

from file_reader import FileReader
from run import Processor

class RunTestCase(unittest.TestCase):
    def setUp(self):
        entries = FileReader('../test-input.txt').process_file()
        self.processor = Processor(entries)

    def test_find_best_pos(self):
        self.processor.decipher_signals()
        self.assertEqual(self.processor.total_output, 61229)
