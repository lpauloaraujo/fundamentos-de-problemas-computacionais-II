from queue import Queue
from utils.dl_list import DL_List

class UAL_Graph:
    def __init__(self):
        self.vertices_list = DL_List()

    def insert_vertex(self, vertex):
        self.vertices_list.insert_at_ending(vertex)

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
            vertexb.edges.insert_at_ending(vertexa)
            return True

    def bfs(self, start_vertex):
        current_vertex = self.vertices_list.beginning
        while current_vertex is not None:
            current_vertex.data.color = 'w'
            current_vertex.data.distance = -1
            current_vertex.data.predecessor = None
            current_vertex = current_vertex.next
        start_vertex.color = 'g'
        start_vertex.distance = 0
        start_vertex.predecessor = None
        queue = Queue()
        queue.put(start_vertex)
        while queue.qsize != 0:
            current_vertex = queue.get()
            current_edge = current_vertex.edges.beginning
            while current_edge is not None:
                if current_edge.data.color == 'w':
                    current_edge.data.color = 'g'
                    current_edge.data.distance = current_vertex.distance + 1
                    current_edge.data.predecessor = current_vertex
                    queue.put(current_edge.data)
                current_edge = current_edge.next
            current_vertex.color = 'b'

    def dfs(self):
        pass

    def dfs_visit(self, vertex):
        pass

    def __str__(self):
        string = ""
        current_vertex = self.vertices_list.beginning
        while current_vertex is not None:
            string += f"{str(current_vertex.data)}"
            current_vertex = current_vertex.next
        return string
