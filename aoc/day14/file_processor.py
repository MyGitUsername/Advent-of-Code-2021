from ..file_reader import FileReader
from typing import Dict

class FileProcessor(FileReader):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.input = super().lines()

    def polymer_template(self) -> str:
        return self.input[0]

    def pair_insertion_rules(self) -> Dict[str, str]:
        relevant_input = self.input[1:]
        pair_insertion_rules = dict()
        for rule in relevant_input:
            k, v = rule.split(' -> ')
            pair_insertion_rules[k] = v
        return pair_insertion_rules
