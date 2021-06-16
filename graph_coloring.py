class Graph:
    def __init__(self, number_of_vertices: int):
        # [0, 0] the first element indicates the adjacency, the second element indicates the color. 0 -> no color.
        self.adjacency_matrix = [[[0, 0] for i in range(number_of_vertices)] for j in range(number_of_vertices)]
        self.number_of_vertices = number_of_vertices
        self.color_set = set(range(1, self.max_degree()+2))
        self.Delta = self.max_degree()

    def add_edge(self, v1: int, v2: int):
        self.adjacency_matrix[v1][v2][0] = 1
        self.adjacency_matrix[v2][v1][0] = 1
        self.max_degree()

    def max_degree(self):
        delta = 0
        for neighbours in self.adjacency_matrix:
            degree = 0
            for neighbour in neighbours:
                degree += neighbour[0]
            if degree > delta:
                delta = degree
        self.color_set = set(range(1, delta + 2))
        self.Delta = delta
        return delta

    def colored_neighbours(self, vertex: int):  # returns [vi, vi+1, ...] such that the (vertex-vi) edge is colored.
        neighbours = []
        for i in range(self.number_of_vertices):
            if self.adjacency_matrix[vertex][i][0] == 1 and self.adjacency_matrix[vertex][i][1] != 0:
                neighbours.append(i)
        return neighbours

    def uncolored_neighbours(self, vertex: int):    # returns [vi, vi+1, ...] such that each (vertex-vi) edge is not colored.
        neighbours = []
        for i in range(self.number_of_vertices):
            if self.adjacency_matrix[vertex][i][0] == 1 and self.adjacency_matrix[vertex][i][1] == 0:
                neighbours.append(i)
        return neighbours

    def free_colors(self, vertex: int): # returns free colors at a given vertex. Refer to the article for more details.
        incident_colors = set()
        for i in range(self.number_of_vertices):
            if self.adjacency_matrix[i][vertex][0] == 1 and self.adjacency_matrix[i][vertex][1] != 0:
                incident_colors.add(self.adjacency_matrix[i][vertex][1])
        return self.color_set - incident_colors


class Fan:
    def __init__(self):
        pass


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


def make_fan(uncolored_f: int, colored_list: list, graph: '__main__.Graph'):
    pass


def invert_cd_path():
    pass


def rotate_and_color():
    pass


def algorithm(graph: '__main__.Graph'):
    for x in range(graph.number_of_vertices):
        for fan_vertices in graph.uncolored_neighbours(x):
            make_fan(graph.colored_neighbours(x), fan_vertices, graph)
            invert_cd_path()
            rotate_and_color()


if __name__ == "__main__":
    graph = get_input()
    for i in range(graph.number_of_vertices):
        print(graph.free_colors(i))
        print(graph.colored_neighbours(i))
        print(graph.uncolored_neighbours(i))
    print("done")




