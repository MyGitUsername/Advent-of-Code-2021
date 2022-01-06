from typing import List, Any

class FileReader:
    def __init__(self, file_name):
        self._file_name = file_name;

    @property
    def file_name(self):
        return self._file_name

    def process_file(self, Class) -> List[Any]:
        with open(self.file_name, 'r') as f:
            lines = f.readlines()
        return [list(Class(int(row_idx), int(col_idx), int(char)) for col_idx, char in enumerate(line[:-1])) for row_idx, line in enumerate(lines)]

    def lines(self) -> List[str]:
        with open(self.file_name, 'r') as f:
            lines = f.readlines()
        return [line.strip() for line in lines if line != '\n']
