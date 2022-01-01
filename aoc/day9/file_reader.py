from location import Location

class FileReader:
    def __init__(self, file_name):
        self._file_name = file_name;

    @property
    def file_name(self):
        return self._file_name

    def process_file(self):
        f = open(self.file_name, 'r')
        lines = f.readlines()
        f.close()
        return [list(Location(int(row), int(col), int(lines[row][col])) for col in range(len(lines[row][:-1]))) for row in range(len(lines))]
