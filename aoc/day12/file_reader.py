from ..file_reader import FileReader

class GraphFileReader(FileReader):
    def process_file(self):
        with open(self.file_name, 'r') as f:
            lines = f.readlines()
        return [tuple(row.strip().split('-')) for row in lines]
