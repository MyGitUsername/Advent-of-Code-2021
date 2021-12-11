from lattern_fish import Fish 

class FileReader:
    def __init__(self, file_name):
        self._file_name = file_name;
        self._lines = []
        self._points = []

    @property
    def file_name(self):
        return self._file_name

    def process_file(self):
        f = open(self.file_name, 'r')
        input = f.readline()[:-1]

        return [Fish(int(timer)) for timer in input.split(',')]
