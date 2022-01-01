class FileReader:
    def __init__(self, file_name):
        self._file_name = file_name;

    @property
    def file_name(self):
        return self._file_name

    def process_file(self):
        f = open(self.file_name, 'r')

        entries = []
        for line in f:
            signal_pattern, four_digit_output = line.split('|')
            entries.append((signal_pattern.strip(), four_digit_output.strip()))

        return entries

