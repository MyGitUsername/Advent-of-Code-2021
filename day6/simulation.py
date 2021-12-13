from file_reader import FileReader
import concurrent.futures
from functools import reduce
from collections import Counter
import copy

class Simulation:
    def __init__(self, fishes, days):
        self.fishes = fishes
        self.days = days
        self.result = 0

    def run(self):
        new_fishes = []
        for _ in range(self.days):
            for fish in self.fishes:
                spawned = fish.get_older()
                if spawned:
                    new_fishes.append(spawned)

            self.fishes = self.fishes + new_fishes
            new_fishes = []

        return self.fishes

    def run2(self):
        fish_dict = Counter(fishes)
        print(f'fish_dict {fish_dict}')
        vals = []
        for fish in fish_dict:
            occurrences  = fish_dict[fish]
            print(f'fish: {fish}, days: {self.days}, num: {occurrences}')
            num_of_offspring = fish.simulate_days(0, self.days)
            print(f'fish_sim: {num_of_offspring}')
            vals.append(num_of_offspring * occurrences)
        return reduce(lambda a, b: a + b, vals)

if __name__ == "__main__":
    fishes = FileReader('input.txt').process_file()
    simulation = Simulation(fishes, 80)
    res = simulation.run2()
    print(f'Result: {res}')
