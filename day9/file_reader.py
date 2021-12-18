class FileReader:
    def __init__(self, file_name):
        self._file_name = file_name;

    @property
    def file_name(self):
        return self._file_name

    def process_file(self):
        f = open(self.file_name, 'r')
        return [list(int(num) for num in line.strip()) for line in f]


