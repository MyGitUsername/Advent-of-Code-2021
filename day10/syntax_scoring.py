from io import UnsupportedOperation
from file_reader import FileReader
import statistics

class SyntaxScoring:
    def __init__(self, nav_sys): 
        self._nav_sys = nav_sys
        self._corrupted_lines = []
        self._incomplete_lines = []
        self._syntax_error_score = 0
        self._autocomplete_scores = []

    @property
    def nav_sys(self):
        return self._nav_sys

    @property
    def corrupted_lines(self):
        return self._corrupted_lines

    @property
    def incomplete_lines(self):
        return self._incomplete_lines

    @property
    def autocomplete_scores(self):
        return self._autocomplete_scores

    @autocomplete_scores.setter
    def autocomplete_scores(self, autocomplete_scores):
        self._autocomplete_scores = autocomplete_scores

    @corrupted_lines.setter
    def corrupted_lines(self, corrupted_lines):
        self._corrupted_lines = corrupted_lines

    @incomplete_lines.setter
    def incomplete_lines(self, incomplete_lines):
        self._incomplete_lines = incomplete_lines

    @property
    def syntax_error_score(self):
        return self._syntax_error_score
                
    @syntax_error_score.setter
    def syntax_error_score(self, syntax_error_score):
        self._syntax_error_score = syntax_error_score
                
    def is_opening_char(self, char):
        return char == '{' or char == '(' or char == '[' or char == '<'

    def is_closing_char(self, char):
        return char == '}' or char == ')' or char == ']' or char == '>'

    def get_match(self, char):
        if char == '{':
            match = '}'
        elif char == '(':
            match = ')'
        elif char == '[': 
            match = ']'
        elif char == '<':
            match = '>'
        elif char == '}':
            match = '{'
        elif char == ')':
            match = '('
        elif char == ']': 
            match = '['
        elif char == '>':
            match = '<'
        else:
            match = False
        return match

    def score(self, closing):
        if closing == ')':
            score = 3
        elif closing == ']': 
            score = 57
        elif closing == '}':
            score = 1197
        elif closing == '>':
            score = 25137 
        else:
            raise UnsupportedOperation('Not a valid closing char')
        return score

    def score_pt2(self, char):
        if char == '(':
            score = 1
        elif char == '[': 
            score = 2
        elif char == '{':
            score = 3
        elif char == '<':
            score = 4 
        else:
            raise UnsupportedOperation('Not a valid closing char')
        return score

    def determine_closing_sequence(self):
        self.autocomplete_scores = []

        if len(self.incomplete_lines) == 0:
            self.identify_incomplete_lines()

        stack = []
        for line in self.incomplete_lines:
            autocomplete_score = 0
            for char in line:
                if self.is_opening_char(char):
                    stack.append(char)
                else:
                    stack.pop()
            
            for char in stack[::-1]:
                autocomplete_score *= 5
                autocomplete_score += self.score_pt2(char)

            stack.clear()
            self.autocomplete_scores.append(autocomplete_score)

    def identify_corrupted_lines(self): 
        self.corrupted_lines = []
        self.syntax_error_score = 0
        stack = []

        for line in self.nav_sys:
            for char in line:
                if self.is_opening_char(char):
                    stack.append(char)
                else:
                    top = stack.pop()
                    if self.get_match(top) != char:
                        self.corrupted_lines.append(line)
                        self.syntax_error_score += self.score(char)
                        break
            stack.clear()

    def identify_incomplete_lines(self):
        if len(self.corrupted_lines) == 0:
            self.identify_corrupted_lines()

        self.incomplete_lines = [line for line in self.nav_sys if line not in self.corrupted_lines]

    def autocomplete_winner(self):
        return statistics.median(map(int, self.autocomplete_scores))

if __name__ == "__main__":
    nav_sys = FileReader('input.txt').process_file()
    syntax_scoring = SyntaxScoring(nav_sys)
    syntax_scoring.determine_closing_sequence()
    print(f'Autocomplete Score: {syntax_scoring.autocomplete_winner()}')
