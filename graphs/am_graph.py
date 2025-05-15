class UAM_Graph:
    def __init__(self, vertices):
        self.vertices_list = vertices
        self.adjacency_matrix = self.create_adjacency_matrix(self.vertices_list)

    def insert_vertex(self, new_vertex):
        self.vertices_list.append(new_vertex)
        self.update_adjacency_matrix(new_vertex)
    
    def create_adjacency_matrix(self, vertices_list):
        matrix = []
        if len(vertices_list) > 0:
            for index, line_vertex in enumerate(self.vertices_list):
                line = [1 if column_vertex in line_vertex.edges else 0 for column_vertex in self.vertices_list[:index + 1]]
                matrix.append(line)
        return matrix

    def update_adjacency_matrix(self, new_vertex):
        new_vertex_line = [1 if vertex in new_vertex.edges else 0 for vertex in self.vertices_list]
        self.adjacency_matrix.append(new_vertex_line)
    