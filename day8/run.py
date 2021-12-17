from file_reader import FileReader

class Processor:
    def __init__(self, entries): 
        self._entries = entries
        self._total_output = 0

    @property
    def total_output(self):
        return self._total_output

    @total_output.setter
    def total_output(self, n):
        self._total_output = n

    @property
    def entries(self):
        return self._entries

    def deduce_uniques(self, pattern, cipher):
        l = len(pattern)
        if l == 2:
            cipher[1] = pattern
        elif l == 3: 
            cipher[7] = pattern
        elif l == 4:
            cipher[4] = pattern
        elif l == 7: 
            cipher[8] = pattern

    def deduce_remaining(self, pattern, cipher):
        l = len(pattern)
        if l == 6 and contains_chars(cipher[1], pattern) and contains_chars(cipher[4], pattern):
            cipher[9] = pattern
        elif l == 6 and contains_chars(cipher[7], pattern):
            cipher[0] = pattern
        elif l == 6:
            cipher[6] = pattern
        elif l == 5 and contains_chars(cipher[1], pattern):
            cipher[3] = pattern
        elif l == 5 and number_of_chars_not_in_string(cipher[4], pattern) == 1:
            cipher[5] = pattern
        else:
            cipher[2] = pattern

    def pattern_to_digit(self, pattern, cipher):
        for key in cipher:
            if is_same_digit(cipher[key], pattern):
                return key

    def calculate_output(self, output, cipher):
        res = '' 
        for pattern in output:
            res += str(self.pattern_to_digit(pattern, cipher))
        return int(res)

    def decipher_signals(self):
        for entry in self.entries:
            signal_pattern = entry[0].split()
            output = entry[1].split()

            cipher = {}
            for pattern in signal_pattern:
                self.deduce_uniques(pattern, cipher)
            for pattern in signal_pattern:
                if pattern not in cipher.values():
                    self.deduce_remaining(pattern, cipher)

            m = self.calculate_output(output, cipher)
            self.total_output += m


def is_same_digit(s1, s2):
    return sorted(s1) == sorted(s2)

def contains_chars(s1, s2):
    for c in s1:
        if c not in s2:
            return False
    return True

def number_of_chars_not_in_string(s1, s2):
    counter = 0
    for c in s1:
        if c not in s2:
            counter += 1
    return counter

if __name__ == "__main__":
    entries = FileReader('input.txt').process_file()
    processor = Processor(entries)
    processor.decipher_signals()
    print(f'total output values: {processor.total_output}')
