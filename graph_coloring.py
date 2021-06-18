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

    def edge_color(self, v1: int, v2: int):
        return self.adjacency_matrix[v1][v2][1]


class Fan:
    def __init__(self, x: int, vertices: list, graph: '__main__.Graph'):
        self.x_vertex = x
        self.l_vertex = vertices[-1]
        self.f_vertex = vertices[0]
        self.vertices = vertices
        self.graph = graph
        self.c_color = list(self.graph.free_colors(self.x_vertex))[0]
        self.d_color = list(self.graph.free_colors(self.l_vertex))[1] if list(self.graph.free_colors(self.l_vertex))[0] == self.c_color\
            else list(self.graph.free_colors(self.l_vertex))[0]

    def invert_cd_path(self):
        start = self.x_vertex
        end_point = self.x_vertex
        while True:
            flag = 0
            for i in range(self.graph.number_of_vertices):
                if self.graph.adjacency_matrix[start][i][0] == 1 and self.graph.adjacency_matrix[start][i][1] == self.c_color:
                    self.graph.adjacency_matrix[start][i][1] = self.d_color
                    start = i
                    flag = 1
                    break
                elif self.graph.adjacency_matrix[start][i][0] == 1 and self.graph.adjacency_matrix[start][i][1] == self.d_color:
                    self.graph.adjacency_matrix[start][i][1] = self.c_color
                    start = i
                    flag = 1
                    break
            if flag == 0:
                break
        return end_point

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


def dfs(start: int, adj_list: list, visited: list, number_of_fan_edges: int, graph: '__main__.Graph'):
    # goal of dfs is to visit all the vertices of fan edges i.e, <f..l>.
    if len(visited) == number_of_fan_edges-1:
        visited.append(start)
        return visited
    else:
        visited.append(start)
        path = []
        for i in adj_list[start]:
            if i not in visited:
                child_result = dfs(i, adj_list, visited[:], number_of_fan_edges, graph)
                if child_result:
                    path = child_result[:]
                    break
        return path


def make_fan(x: int, uncolored_f: int, colored_list: list, graph: '__main__.Graph'):
    adj_list = [[] for i in range(graph.number_of_vertices)]
    temp_list = colored_list[:]
    temp_list.append(uncolored_f)
    # construct a graph of possible combinations of edges(vertices) in a fan
    for i in temp_list:
        for j in graph.free_colors(i):
            for k in temp_list:
                if j == graph.edge_color(x, k):
                    adj_list[i].append(k)
    fan_vertices = dfs(uncolored_f, adj_list, [], len(temp_list), graph)
    fan = Fan(x, fan_vertices, graph)
    return fan


def algorithm(graph: '__main__.Graph'):
    for x in range(graph.number_of_vertices):
        for fan_vertices in graph.uncolored_neighbours(x):
            fan = make_fan(x, fan_vertices, graph.colored_neighbours(x), graph)
            fan.invert_cd_path()
            # rotate_and_color()


if __name__ == "__main__":
    # graph = get_input()
    input_graph = Graph(4)
    test = [[[0,0], [1,4],[0,0], [1,2]],\
            [[1,4], [0,0],[1,0], [1,3]],\
            [[0,0], [1,0],[0,0], [1,0]],\
            [[1,0], [1,3], [1,0], [0,0]]]
    input_graph.adjacency_matrix = test
    input_graph.number_of_vertices = 4
    input_graph.Delta = 3
    input_graph.color_set = {1, 2, 3, 4}
    make_fan(1, 2, input_graph.colored_neighbours(1), input_graph).invert_cd_path()
    print("j")




