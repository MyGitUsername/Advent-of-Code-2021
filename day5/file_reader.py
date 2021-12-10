from point import Point
from functools import reduce
from collections import Counter

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

        point_pairs = []
        # lines = []
        for line in f:
            [point1, point2] = line.split('->')
            [x1, y1] = point1[:-1].split(',')
            [x2, y2] = point2[1:].split(',')
            point_pairs.append((Point(int(x1), int(y1)), Point(int(x2), int(y2))))

        return point_pairs

if __name__ == "__main__":
    file_reader = FileReader('input.txt')
    point_pairs = file_reader.process_file()
    only_lines = [(p1, p2) for p1, p2 in point_pairs if p1.is_line(p2)]
    all_points = reduce(lambda l1, l2: l1 + l2, 
                        (p1.points_in_line(p2) for p1, p2 in only_lines))
    occurrences = Counter(all_points)


    number_of_times_point_appears_at_least_twice = len([v for v in occurrences.values() if v >= 2 ]) 
    print(number_of_times_point_appears_at_least_twice) 
    
