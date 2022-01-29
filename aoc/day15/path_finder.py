from ..file_reader import FileReader
from ..cell import Cell
from .cavern import Cavern
import os
import sys
from typing import Set

class Pathfinder:
    def __init__(self, cavern: Cavern):
        self.cavern = cavern
        
    def dijkstra(self) -> int:
        visited: Set[Cell] = set()
        unvisited: Set[Cell] = set(self.cavern.flatten())
        start_vertex: Cell = self.cavern.get_cell(0, 0)

        # TODO: figure out whil zip creates shallow copy of each fillvalue
        # table = dict(itertools.zip_longest(unvisited, {}, fillvalue=copy.deepcopy({'min_dist': sys.maxsize, 'prev_vertex': None})))
        table = dict()
        for v in unvisited:
            table[v] = {'min_dist': sys.maxsize, 'prev_vertex': None}
        table[start_vertex]['min_dist'] = 0
        
        while len(unvisited) != 0:
            current_vertex =  self.visit_closest(unvisited, table)
            unvisited_neighbors = set(self.cavern.get_adjacent_locs(current_vertex)) & unvisited
            for neighbor in unvisited_neighbors:
                distance_to_start = table[current_vertex]['min_dist'] + neighbor.value
                if distance_to_start < table[neighbor]['min_dist']:
                    table[neighbor]['min_dist'] = distance_to_start
                    table[neighbor]['prev_vertex'] = current_vertex
            visited.add(current_vertex)
            unvisited.remove(current_vertex)

        return table[self.cavern.end()]['min_dist']


    def visit_closest(self, unvisited, table):
        return min(unvisited, key=lambda x: table[x]['min_dist'])

if __name__ == "__main__":
    fr = FileReader(os.path.dirname(__file__) + '/input.txt')
    cells = fr.process_file(Cell)
    pf = Pathfinder(Cavern(cells))
    shortest_path = pf.dijkstra()
    print(f'shortest_path: {shortest_path}')
