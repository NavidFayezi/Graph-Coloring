class Graph:
    def __init__(self, number_of_vertices: int):
        self.adjacency_matrix = [[[0, None] for i in range(number_of_vertices)] for j in range(number_of_vertices)]

    def add_edge(self, v1: int, v2: int):
        self.adjacency_matrix[v1][v2][0] = 1
        self.adjacency_matrix[v2][v1][0] = 1

    def max_degree(self):
        delta = 0
        for neighbours in self.adjacency_matrix:
            degree = 0
            for neighbour in neighbours:
                degree += neighbour[0]
            if degree > delta:
                delta = degree
        return delta


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
    return graph


if __name__ == "__main__":
    graph = get_input()
    p = graph.adjacency_matrix[0][0]
    max_degree = graph.max_degree()
    colors = range(1, max_degree+2)

