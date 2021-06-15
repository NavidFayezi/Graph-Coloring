"""class Edge:
    def __init__(self, v1: '__main__.Vertex', v2: '__main__.Vertex'):
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

"""


class Graph:
    def __init__(self, number_of_vertices: int):
        self.adjacency_matrix = [[[0, None] for i in range(number_of_vertices)] for j in range(number_of_vertices)]

    def add_edge(self, v1: int, v2: int):
        self.adjacency_matrix[v1][v2][0] = 1
        self.adjacency_matrix[v2][v1][0] = 1


def get_input():
    input_line = input()
    input_line = input_line.split(" ")
    assert len(input_line) == 2
    number_of_vertices = int(input_line[0])
    number_of_edges = int(input_line[1])
    graph = Graph(number_of_vertices)
    for i in range(number_of_edges):
        vertices = input().split(" ")
        assert len(vertices) == 2
        v1 = int(vertices[0])
        v2 = int(vertices[1])
        graph.add_edge(v1, v2)


get_input()
