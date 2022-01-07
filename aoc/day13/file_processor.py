from ..file_reader import FileReader
from typing import List, Tuple, Set

class FileProcessor(FileReader):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.input = super().lines()

    def is_dot(self, row) -> bool:
        return row[0] != 'f' and row[0] != '\n'

    def is_folding_instruction(self, row) -> bool:
        return row[0] == 'f'

    def parse_folding_instruction(self, row) -> Tuple[str, int]:
        _, _, instruction = row.split()
        direction, line = instruction.split('=')
        return (direction, int(line))
        
    def dots(self) -> Set[Tuple[int, int]]:
        res = set()
        for row in self.input: 
            if self.is_dot(row):
                x, y = row.strip().split(',')
                res.add((int(x), int(y)))
        return res

    def instructions(self) -> List[Tuple[str, int]]:
        return [self.parse_folding_instruction(row) for row in self.input if self.is_folding_instruction(row)]
