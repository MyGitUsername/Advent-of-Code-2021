from file_reader import FileReader
from functools import reduce

class LavaTubes:
    def __init__(self, heat_map): 
        self._heat_map = heat_map
        self._low_points = set()
        self._basins = list()

    @property
    def heat_map(self):
        return self._heat_map

    @property
    def low_points(self):
        return self._low_points

    @property
    def basins(self):
        return self._basins

    @low_points.setter
    def low_points(self, low_points):
        self._low_points = low_points

    @basins.setter
    def basins(self, basins):
        self._basins = basins

    def row_length(self):
        return len(self.heat_map[0])

    def col_length(self):
        return len(self.heat_map)

    def is_left_edge(self, loc):
        return loc.col_idx == 0

    def is_right_edge(self, loc):
        return loc.col_idx == self.row_length() - 1

    def is_top_edge(self, loc):
        return loc.row_idx == 0

    def is_bottom_edge(self, loc):
        return loc.row_idx == self.col_length() - 1

    def get_loc_above(self, loc):
        return self.heat_map[loc.row_idx - 1][loc.col_idx]

    def get_loc_below(self, loc):
        return self.heat_map[loc.row_idx + 1][loc.col_idx]

    def get_loc_right(self, loc):
        return self.heat_map[loc.row_idx][loc.col_idx + 1]

    def get_loc_left(self, loc):
        return self.heat_map[loc.row_idx][loc.col_idx - 1]

    def get_adjacent_locs(self, loc):
        adjacent_locs = []
        
        if not self.is_top_edge(loc):
            adjacent_locs.append(self.get_loc_above(loc))
        if not self.is_bottom_edge(loc):
            adjacent_locs.append(self.get_loc_below(loc))
        if not self.is_right_edge(loc):
            adjacent_locs.append(self.get_loc_right(loc))
        if not self.is_left_edge(loc):
            adjacent_locs.append(self.get_loc_left(loc))

        return adjacent_locs

    def is_low_point(self, curr_loc, adjacent_locs):
        for adjacent_loc in adjacent_locs:
            if adjacent_loc <= curr_loc:
                return False
        return True
    
    def find_low_points(self):
        for row_idx in range(len(self.heat_map)):
            for col_idx in range(len(self.heat_map[row_idx])):
                curr_loc = self.heat_map[row_idx][col_idx]
                adjacent_locs = self.get_adjacent_locs(curr_loc)
                if self.is_low_point(curr_loc, adjacent_locs):
                    self.low_points.add(curr_loc)

    def find_basin(self, low_point):
        basin = set()
        self.find_basin_aux(low_point, basin)

        return basin

    def find_basin_aux(self, loc, basin):
        if loc not in basin and loc.height != 9:
            basin.add(loc)
            adjacent_locs = self.get_adjacent_locs(loc)
            for adjacent_loc in adjacent_locs:
                self.find_basin_aux(adjacent_loc, basin)

    def find_basins(self):
        if len(self.low_points) == 0:
            self.find_low_points()

        for lp in self.low_points:
            self.basins.append(self.find_basin(lp))

    def sum_of_risk_lvl(self):
        return 1 + reduce(lambda a, b: (1 + a + b), [lp.height for lp in self.low_points])

    def find_three_largest_basins(self):
        sorted_basins = sorted(self.basins, key=lambda a: len(a), reverse=True)
        return sorted_basins[0], sorted_basins[1], sorted_basins[2]

    def result_part_two(self):
        return reduce(lambda a, b: a * b, [len(basin) for basin in self.find_three_largest_basins()])
                
if __name__ == "__main__":
    heat_map = FileReader('input.txt').process_file()
    lava_tubes = LavaTubes(heat_map)
    lava_tubes.find_low_points() 
    lava_tubes.find_basins() 
    print(f'sum of risk: {lava_tubes.sum_of_risk_lvl()}')
    print(f'low_points: {lava_tubes.low_points}')
    print(f'basins: {lava_tubes.basins}')
    print(f'result part two: {lava_tubes.result_part_two()}')
