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

    def add_adjacency(self, vertex: '__main__.Vertex'):
        self.adjacencies.append(vertex)


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.delta = 0


def get_input():
    input_line = input()
    input_line.split(" ")
    print(input_line)



