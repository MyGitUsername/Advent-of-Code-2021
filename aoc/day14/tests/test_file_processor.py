import unittest
import os
from ..file_processor import FileProcessor

class FileProcessorTestCase(unittest.TestCase):
    def setUp(self):
        self.file_processor = FileProcessor(os.path.dirname(__file__) + '/tiny-input.txt')

    def test_polymer_template(self):
        actual = self.file_processor.polymer_template()
        self.assertEqual(actual, 'NNCB')

    def test_instructions(self):
        actual = self.file_processor.pair_insertion_rules()
        expected = {'CH': 'B','HH': 'N', 'CB': 'H'}
        self.assertEqual(actual, expected)
