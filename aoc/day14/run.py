from .file_processor import FileProcessor
import os
import sys
from collections import Counter
from multiprocessing import Pool 
import os
import pdb

class Run():
    def __init__(self, polymer_template, rules):
        self.polymer_template = polymer_template
        self.rules = rules
        self.final_polymer = self.polymer_template

    def execute_rule(self, idx):
        print('process id:', os.getpid())
        pair = self.final_polymer[idx] + self.final_polymer[idx + 1]
        try:
            insert = self.rules[pair]
            return insert + pair[1] 
        except:
            print('Error should not be here!')
            # pdb.set_trace()
            return pair[1]
    
    # NNCB
    def run(self, steps = sys.maxsize):
        for step in range(0, steps):
            modified_polymer = []
            with Pool(processes=4) as pool:
                modified_polymer = pool.map(self.execute_rule, range(len(self.final_polymer) - 1))
            self.final_polymer =  self.final_polymer[0] + ''.join(modified_polymer) 
            # pdb.set_trace()
            print(f'self.final_polymer {self.final_polymer}')
            print(f'step {step} complete')

    def get_result(self):
        if self.final_polymer == self.polymer_template:
            raise RuntimeError('The run method needs to execute before calling get_results()')
        counter = Counter(self.final_polymer)
        _, most_common = counter.most_common()[0]
        _, least_common = counter.most_common()[-1]
        return most_common - least_common


    
if __name__ == "__main__":
    fp = FileProcessor(os.path.dirname(__file__) + '/input.txt')
    run = Run(fp.polymer_template(), fp.pair_insertion_rules())
    run.run(20)
    result = run.get_result()
    print(f' res: {result}')
