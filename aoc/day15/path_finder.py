from ..file_reader import FileReader
from ..cell import Cell
from .cavern import Cavern
import os
import sys
from typing import Set
import heapq

class Pathfinder:
    def __init__(self, cavern: Cavern):
        self.cavern = cavern
        
    def dijkstra_with_priority_queue(self) -> int:
        visited: Set[Cell] = set()
        start_vertex: Cell = self.cavern.get_cell(0, 0)
        dist = dict()

        table = []
        for v in self.cavern.flatten():
            if v == start_vertex:
                heapq.heappush(table, (0, v))
                continue
            heapq.heappush(table, (sys.maxsize, v))
            dist[v] = sys.maxsize
        
        while len(table) != 0:
            min_dist, current_vertex =  heapq.heappop(table)
            neighbors = [v for v in self.cavern.get_adjacent_locs(current_vertex)]
            for neighbor in neighbors:
                if neighbor not in visited:
                    distance_to_start = min_dist + neighbor.value
                    if distance_to_start < dist[neighbor]:
                        dist[neighbor] = distance_to_start
                        heapq.heappush(table, (distance_to_start, neighbor))
            visited.add(current_vertex)

        return dist[self.cavern.end()]
        
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
            unvisited_neighbors = [v for v in self.cavern.get_adjacent_locs(current_vertex) if table[v]['prev_vertex'] == None]
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
    small_cavern = Cavern(cells)
    large_cavern = small_cavern.gen_large_cavern()
    pf = Pathfinder(large_cavern)
    shortest_path = pf.dijkstra_with_priority_queue()
    print(f'shortest_path: {shortest_path}')
