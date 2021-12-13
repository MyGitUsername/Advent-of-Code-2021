from file_reader import FileReader
import sys
import math

PART_2 = 2
PART_1 = 1

class Simulation:
    def __init__(self, crabs, version):
        self.best_pos = 0
        self.crabs = crabs
        self.min_fuel_usage = sys.maxsize
        self.version = version

    # nth triangle number formula
    def calculate_fuel_part_2(self, origin, dest):
        n = abs(origin - dest)
        return (math.pow(n, 2) + n) / 2

    def calculate_fuel_part_1(self, origin, dest):
        return abs(origin - dest) 

    def calculate_fuel(self, origin, dest):
        if self.version == PART_1:
            return self.calculate_fuel_part_1(origin, dest) 
        return self.calculate_fuel_part_2(origin, dest)

    def find_best_pos(self):
        # pdb.set_trace()
        min_hor_pos = min(self.crabs)
        max_hor_pos = max(self.crabs)
        for dest in range(min_hor_pos, max_hor_pos + 1):
            total_fuel_usage = 0
            for origin in self.crabs:
                fuel_usage = self.calculate_fuel(origin, dest)
                total_fuel_usage += fuel_usage
                if (total_fuel_usage > self.min_fuel_usage):
                    break

            if (total_fuel_usage < self.min_fuel_usage):
                self.best_pos = dest
                self.min_fuel_usage = total_fuel_usage

    def find_best_pos_part_1(self):
        # pdb.set_trace()
        min_hor_pos = min(self.crabs)
        max_hor_pos = max(self.crabs)
        for dest in range(min_hor_pos, max_hor_pos + 1):
            total_fuel_usage = 0
            for origin in self.crabs:
                fuel_usage = abs(origin - dest) 
                total_fuel_usage += fuel_usage
                if (total_fuel_usage > self.min_fuel_usage):
                    break

            if (total_fuel_usage < self.min_fuel_usage):
                self.best_pos = dest
                self.min_fuel_usage = total_fuel_usage

if __name__ == "__main__":
    crabs = FileReader('input.txt').process_file()
    sim = Simulation(crabs, 2)
    sim.find_best_pos()
    print(f'\n-------\nResults\n-------')
    print(f'best_position: {sim.best_pos}, fuel_usage: {sim.min_fuel_usage}')
