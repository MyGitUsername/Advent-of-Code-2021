from file_reader import FileReader
import pdb
import sys

class Simulation:
    def __init__(self, crabs):
        self.best_pos = 0
        self.crabs = crabs
        self.min_distance_to_dest = sys.maxsize

    def find_best_pos(self):
        # pdb.set_trace()
        min_hor_pos = min(self.crabs)
        max_hor_pos = max(self.crabs)
        for dest in range(min_hor_pos, max_hor_pos + 1):
            total_distance_to_dest = 0
            for curr_pos in self.crabs:
                dist_to_dest = abs(curr_pos - dest) 
                total_distance_to_dest += dist_to_dest
                if (total_distance_to_dest > self.min_distance_to_dest):
                    break

            if (total_distance_to_dest < self.min_distance_to_dest):
                self.best_pos = dest
                self.min_distance_to_dest = total_distance_to_dest

        

if __name__ == "__main__":
    crabs = FileReader('input.txt').process_file()
    sim = Simulation(crabs)
    sim.find_best_pos()
    print(f'\n-------\nResults\n-------')
    print(f'best_position: {sim.best_pos}, fuel_usage: {sim.min_distance_to_dest}')
