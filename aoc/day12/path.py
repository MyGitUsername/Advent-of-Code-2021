import copy
import networkx as nx
from .file_reader import GraphFileReader
import os


class Path:
    def __init__(self, edges):
        self.G = nx.Graph()
        self.paths = []
        self.G.add_edges_from(edges)

    def is_small_cave(self, n):
        return n.islower()

    def visited_small_cave(self, n, path):
        return self.is_small_cave(n) and n in path

    def can_visit(self, n, path):
        return not self.visited_small_cave(n, path)

    def find_paths(self):
        self.find_paths_aux('start', ['start'])

    def find_paths_aux(self, n, path):
        if n == 'end':
            self.paths.append(copy.deepcopy(path))
            return

        neighbors  = self.G.neighbors(n)
        for neighbor in neighbors:
            if self.can_visit(neighbor, path):
                path.append(neighbor)
                self.find_paths_aux(neighbor, path)
                path.pop()


if __name__ == "__main__":
    edges = GraphFileReader(os.path.dirname(__file__) + '/input.txt').process_file()
    path_finder = Path(edges)
    path_finder.find_paths()
    print(f'Number of Paths: {len(path_finder.paths)}')

