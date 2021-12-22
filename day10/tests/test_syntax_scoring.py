import unittest
import os
import sys
sys.path.append(os.path.abspath('..'))

from file_reader import FileReader
from syntax_scoring import SyntaxScoring

class SimulationTestCase(unittest.TestCase):
    def setUp(self):
        self.file_reader = FileReader('test-input.txt')

    def test_syntax_scoring(self):
        nav_sys = self.file_reader.process_file()
        ss = SyntaxScoring(nav_sys)
        ss.identify_corrupted_lines()
        self.assertEqual(ss.syntax_error_score, 26397)
