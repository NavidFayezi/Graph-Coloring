class Edge:
    def __init__(self, v1: int, v2: int):
        self.vertices = {v1, v2}
        self.edge_color = None          # for the sake of simplicity colors are assumed to be integers

    def color(self, color: int):
        self.edge_color = color


class Vertex:
    def __init__(self, v: int):
        self.vertex_number = v
        self.adjacencies = []
        self.degree = 0

    def add_adjacency(self, vertex: '__main__.Vertex'):
        if vertex not in self.adjacencies:
            self.adjacencies.append(vertex)
            self.degree += 1


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.min_degree = 0


def get_input():
    input_line = input()
    input_line = input_line.split(" ")
    assert len(input_line) == 2
    number_of_vertices = int(input_line[0])
    number_of_edges = int(input_line[1])


get_input()
