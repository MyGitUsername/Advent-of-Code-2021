from .file_processor import FileProcessor
import os
import sys
from collections import Counter
import pdb

class Run():
    def __init__(self, polymer_template, rules):
        self.polymer_template = polymer_template
        self.rules = rules
        
    def execute_rule(self, pair):
        try:
            insert = self.rules[pair]
            return insert + pair[1] 
        except:
            return pair[1]

    
    def run(self, steps = sys.maxsize):
        new_polymer = self.polymer_template
        for _ in range(0, steps):
            modified_polymer = new_polymer[0]
            for j in range(len(new_polymer) - 1):
                pair = new_polymer[j] + new_polymer[j + 1]
                modified_polymer += self.execute_rule(pair)
            new_polymer = modified_polymer
        return new_polymer

    def get_result(self, polymer):
        counter = Counter(polymer)
        _, most_common = counter.most_common(1)[0]
        _, least_common = counter.most_common()[-1]
        return most_common - least_common


    
if __name__ == "__main__":
    fp = FileProcessor(os.path.dirname(__file__) + '/input.txt')
    run = Run(fp.polymer_template(), fp.pair_insertion_rules())
    final_polymer = run.run(40)
    result = run.get_result(final_polymer)
    print(f' res: {result}')
