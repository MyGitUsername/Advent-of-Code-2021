class TwoDimensionalArray:
    def __init__(self, two_dimensional_array): 
        self._two_dimensional_array = two_dimensional_array

    @property
    def two_dimensional_array(self):
        return self._two_dimensional_array

    def row_length(self):
        return len(self.two_dimensional_array[0])

    def col_length(self):
        return len(self.two_dimensional_array)

    def get_cell(self, row_idx, col_idx):
        return self.two_dimensional_array[row_idx][col_idx]

    def flatten(self):
        return [item for sub_list in self.two_dimensional_array for item in sub_list]

    def is_left_edge(self, loc):
        return loc.col_idx == 0

    def is_right_edge(self, loc):
        return loc.col_idx == self.row_length() - 1

    def is_top_edge(self, loc):
        return loc.row_idx == 0

    def is_bottom_edge(self, loc):
        return loc.row_idx == self.col_length() - 1

    def get_top(self, loc):
        return self.two_dimensional_array[loc.row_idx - 1][loc.col_idx]

    def get_bottom(self, loc):
        return self.two_dimensional_array[loc.row_idx + 1][loc.col_idx]

    def get_right(self, loc):
        return self.two_dimensional_array[loc.row_idx][loc.col_idx + 1]

    def get_left(self, loc):
        return self.two_dimensional_array[loc.row_idx][loc.col_idx - 1]

    def get_top_right(self, loc):
        return self.two_dimensional_array[loc.row_idx - 1][loc.col_idx + 1]

    def get_top_left(self, loc):
        return self.two_dimensional_array[loc.row_idx - 1][loc.col_idx - 1]

    def get_bottom_right(self, loc):
        return self.two_dimensional_array[loc.row_idx + 1][loc.col_idx + 1]

    def get_bottom_left(self, loc):
        return self.two_dimensional_array[loc.row_idx + 1][loc.col_idx - 1]

    # Returns all adjacent locations including diagonally adjacent
    def get_all_surounding_locs(self, loc):
        horizontally_and_vertically_adjacent_locs = self.get_adjacent_locs(loc)
        diagonally_adjacent_locs = []

        if not self.is_top_edge(loc) and not self.is_right_edge(loc):
            diagonally_adjacent_locs.append(self.get_top_right(loc))
        if not self.is_top_edge(loc) and not self.is_left_edge(loc):
            diagonally_adjacent_locs.append(self.get_top_left(loc))
        if not self.is_bottom_edge(loc) and not self.is_left_edge(loc):
            diagonally_adjacent_locs.append(self.get_bottom_left(loc))
        if not self.is_bottom_edge(loc) and not self.is_right_edge(loc):
            diagonally_adjacent_locs.append(self.get_bottom_right(loc))

        return horizontally_and_vertically_adjacent_locs + diagonally_adjacent_locs

    # Returns all horizontally and veritically adjacent locations
    def get_adjacent_locs(self, loc):
        adjacent_locs = []
        
        if not self.is_top_edge(loc):
            adjacent_locs.append(self.get_top(loc))
        if not self.is_bottom_edge(loc):
            adjacent_locs.append(self.get_bottom(loc))
        if not self.is_right_edge(loc):
            adjacent_locs.append(self.get_right(loc))
        if not self.is_left_edge(loc):
            adjacent_locs.append(self.get_left(loc))

        return adjacent_locs

    def __repr__(self) -> str:
        return str(self.two_dimensional_array)
