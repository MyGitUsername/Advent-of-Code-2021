class FileReader:
    def __init__(self, file_name):
        self._file_name = file_name;

    @property
    def file_name(self):
        return self._file_name

    def process_file(self):
        f = open(self.file_name, 'r')
        processed_file = [list(char for char in line.strip()) for line in f]
        f.close()
        return processed_file
