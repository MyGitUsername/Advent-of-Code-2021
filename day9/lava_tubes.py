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
        return len(self.heat_map)

    def col_length(self):
        return len(self.heat_map[0])

    def is_left_edge(self, row_index):
        return row_index == 0

    def is_right_edge(self, row_index):
        return row_index == self.row_length() - 1

    def is_top_edge(self, col_index):
        return col_index == 0

    def is_bottom_edge(self, col_index):
        return col_index == self.col_length() - 1

    def is_top_left_corner(self, row_index, col_index):
        return self.is_top_edge(col_index) and self.is_left_edge(row_index)

    def is_bottom_left_corner(self, row_index, col_index):
        return self.is_bottom_edge(col_index) and self.is_left_edge(row_index)

    def is_top_right_corner(self, row_index, col_index):
        return self.is_top_edge(col_index) and self.is_right_edge(row_index)
        
    def is_bottom_right_corner(self, row_index, col_index):
        return self.is_bottom_edge(col_index) and self.is_right_edge(row_index)
    
    def get_adjacent_locations(self, row_index, col_index):
        adjacent_locations = []
        if self.is_top_left_corner(row_index, col_index):
            adjacent_locations.append(self.heat_map[row_index + 1][col_index])
            adjacent_locations.append(self.heat_map[row_index][col_index + 1])
        elif self.is_top_right_corner(row_index, col_index):
            adjacent_locations.append(self.heat_map[row_index - 1][col_index])
            adjacent_locations.append(self.heat_map[row_index][col_index + 1])
        elif self.is_bottom_right_corner(row_index, col_index):
            adjacent_locations.append(self.heat_map[row_index - 1][col_index])
            adjacent_locations.append(self.heat_map[row_index][col_index - 1])
        elif self.is_bottom_left_corner(row_index, col_index):
            adjacent_locations.append(self.heat_map[row_index + 1][col_index])
            adjacent_locations.append(self.heat_map[row_index][col_index - 1])
        elif self.is_top_edge(col_index):
            adjacent_locations.append(self.heat_map[row_index - 1][col_index])
            adjacent_locations.append(self.heat_map[row_index + 1][col_index])
            adjacent_locations.append(self.heat_map[row_index][col_index + 1])
        elif self.is_bottom_edge(col_index):
            adjacent_locations.append(self.heat_map[row_index - 1][col_index])
            adjacent_locations.append(self.heat_map[row_index + 1][col_index])
            adjacent_locations.append(self.heat_map[row_index][col_index - 1])
        elif self.is_left_edge(row_index):
            adjacent_locations.append(self.heat_map[row_index][col_index + 1])
            adjacent_locations.append(self.heat_map[row_index][col_index - 1])
            adjacent_locations.append(self.heat_map[row_index + 1][col_index])
        elif self.is_right_edge(row_index):
            adjacent_locations.append(self.heat_map[row_index][col_index + 1])
            adjacent_locations.append(self.heat_map[row_index][col_index - 1])
            adjacent_locations.append(self.heat_map[row_index - 1][col_index])
        else:
            adjacent_locations.append(self.heat_map[row_index - 1][col_index])
            adjacent_locations.append(self.heat_map[row_index + 1][col_index])
            adjacent_locations.append(self.heat_map[row_index][col_index - 1])
            adjacent_locations.append(self.heat_map[row_index][col_index + 1])
        return adjacent_locations 

    def is_low_point(self, curr_location, locations):
        for location in locations:
            if location <= curr_location:
                return False
        return True

    def find_low_points(self):
        for row_index in range(len(self.heat_map)):
            # print(f' row index {row_index}')
            for col_index in range(len(self.heat_map[row_index])):
                # print(f' col index {col_index}')
                adjacent_locations = self.get_adjacent_locations(row_index, col_index)
                curr_location = self.heat_map[row_index][col_index]
                if self.is_low_point(self.heat_map[row_index][col_index], adjacent_locations):
                    self.low_points += (1 + curr_location)

if __name__ == "__main__":
    heat_map = FileReader('input.txt').process_file()
    lava_tubes = LavaTubes(heat_map)
    lava_tubes.find_low_points() 
    print(f'total number of low points: {lava_tubes.low_points}')
