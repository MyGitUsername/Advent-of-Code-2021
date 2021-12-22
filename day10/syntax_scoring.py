from io import UnsupportedOperation
from file_reader import FileReader

class SyntaxScoring:
    def __init__(self, nav_sys): 
        self._nav_sys = nav_sys
        self._syntax_error_score = 0

    @property
    def nav_sys(self):
        return self._nav_sys

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

    def identify_corrupted_lines(self): 
        stack = []
        for line in self.nav_sys:
            for char in line:
                if self.is_opening_char(char):
                    stack.append(char)
                else:
                    top = stack.pop()
                    if self.get_match(top) != char:
                        self.syntax_error_score += self.score(char)
                        break
            stack.clear()


if __name__ == "__main__":
    nav_sys = FileReader('input.txt').process_file()
    syntax_scoring = SyntaxScoring(nav_sys)
    syntax_scoring.identify_corrupted_lines()
    print(f'Syntax Error Score: {syntax_scoring.syntax_error_score}')
