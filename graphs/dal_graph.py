from graphs.ual_graph import UAL_Graph

class DAL_Graph(UAL_Graph):
    def __init__():
        super().__init__()
    
    def insert_edges(self, edges):
        vertexa = None
        vertexb = None
        vertexaid, vertexbid = edges
        current_vertex = self.vertices_list.beginning

        while vertexa is None and vertexb is None:
            if current_vertex.data.id == vertexaid:
                vertexa = current_vertex
            elif current_vertex.data.id == vertexbid:
                vertexb = current_vertex
            current_vertex = current_vertex.next
        
        if vertexa is None or vertexb is None:
            print("Um ou mais dos dois vértices a formarem a aresta não existem.")
            return False
        
        else:
            vertexa.edges.insert_at_ending(vertexb)
            return True
            