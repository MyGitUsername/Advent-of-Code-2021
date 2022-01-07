from .file_processor import FileProcessor
import os
import sys

class Origami():
    def __init__(self, dots, instructions):
        self.dots = dots
        self.instructions = instructions
        
    def number_of_dots(self):
        return len(self.dots)

    def transpose_up(self, dot, line_of_sym):
        x, y = dot
        y = line_of_sym * 2 - y
        return x, y

    def transpose_right(self, dot, line_of_sym):
        x, y = dot
        x = line_of_sym * 2 - x
        return x, y

    def transpose(self, dot, direction, line_of_sym):
        x, y = dot
        if direction == 'y' and y > line_of_sym:
            return self.transpose_up(dot, line_of_sym)
        elif direction == 'x'and x < line_of_sym:
            return self.transpose_right(dot, line_of_sym)
        return dot
    
    def simulate(self, num_folds = sys.maxsize):
        for idx, instruction in enumerate(self.instructions):
            if idx == num_folds:
                break
            direction, position = instruction
            transposed_dots = set()
            for dot in self.dots:
                transposed = self.transpose(dot, direction, position)
                transposed_dots.add(transposed) 
            self.dots = transposed_dots

if __name__ == "__main__":
    fp = FileProcessor(os.path.dirname(__file__) + '/input.txt')
    origami = Origami(fp.dots(),fp.instructions())
    origami.simulate(1)
    print(f'Number of dots visible: {origami.number_of_dots()}')

