import multiprocessing
from .file_processor import FileProcessor
import os
import sys
from collections import Counter
from multiprocessing import Pool
from collections import Counter 
import os
import time

class Run():
    def __init__(self, polymer_template, rules):
        self.polymer_template = polymer_template
        self.rules = rules
        self.final_polymer = self.polymer_template
        self.counter = Counter(self.polymer_template)

    def execute_rule(self, idx):
        pair = self.final_polymer[idx] + self.final_polymer[idx + 1]
        insert = self.rules[pair]
        self.counter.update(insert)
        return insert + pair[1] 

    def run(self, steps = sys.maxsize):
        num_workers = multiprocessing.cpu_count()  

        for step in range(0, steps):
            modified_polymer = []
            with Pool(num_workers) as pool:
                modified_polymer = pool.map(self.execute_rule, range(len(self.final_polymer) - 1))

            self.final_polymer =  self.final_polymer[0] + ''.join(modified_polymer) 
            # print(f'step {step} complete')

    def get_result(self):
        if self.final_polymer == self.polymer_template:
            raise RuntimeError('The run method needs to execute before calling get_results()')
        counter = Counter(self.final_polymer)
        _, most_common = counter.most_common()[0]
        _, least_common = counter.most_common()[-1]
        return most_common - least_common

    def run_recursive(self, steps):
        for i in range(len(self.final_polymer) - 1):
            pair = self.final_polymer[i] + self.final_polymer[i + 1]
            self.insert_pair(pair, steps)

    def insert_pair(self, pair, steps):
        if (steps == 0):
            return 
        else:
            insert = self.rules[pair]
            self.counter.update(insert)
            self.insert_pair(pair[0] + insert, steps - 1)
            self.insert_pair(insert + pair[1], steps - 1)
    
    def get_result_recursive(self):
        _, most_common = self.counter.most_common()[0]
        _, least_common = self.counter.most_common()[-1]
        return most_common - least_common


if __name__ == "__main__":
    fp = FileProcessor(os.path.dirname(__file__) + '/input.txt')
    run = Run(fp.polymer_template(), fp.pair_insertion_rules())

    # st = time.time()
    # run.run(10)
    # et = time.time()
    # result = run.get_result()
    # print(f'run reg took {et - st}')
    # print(f' res: {result}')

    st = time.time()
    run.run_recursive(20)
    et = time.time()
    result = run.get_result_recursive()
    print(f'run rec took {et - st}')
    print(f' res: {result}')
