from file_reader import FileReader

class LavaTubes:
    def __init__(self, heat_map): 
        self._heat_map = heat_map
        self._low_points = 0

    @property
    def heat_map(self):
        return self._heat_map

    @property
    def low_points(self):
        return self._low_points

    @low_points.setter
    def low_points(self, low_points):
        self._low_points = low_points

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
                    self.low_points += (1 + curr_loc.height)

if __name__ == "__main__":
    heat_map = FileReader('tests/test-input.txt').process_file()
    lava_tubes = LavaTubes(heat_map)
    lava_tubes.find_low_points() 
    print(f'total number of low points: {lava_tubes.low_points}')
