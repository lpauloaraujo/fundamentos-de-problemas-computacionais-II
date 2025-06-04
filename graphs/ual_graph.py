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
        
        size = float(input("Edge size: "))
        edge = {"vertexa": vertexa, "vertexb": vertexb, "size": size}

        
        vertexa.edges.insert_at_ending(edge)
        vertexb.edges.insert_at_ending(edge)
        return True

    def get_edges(self):
        edges = []
        current_vertex = self.vertices_list.beginning
        while current_vertex is not None:
            current_edge = current_vertex.data.edges.beggining
            while current_edge is not None:
                if current_edge not in edges:
                    edges.append(current_edge)
        return edges

    def get_sorted_edges(self):
        edges = self.get_edges
        sorted_edges = sorted(edges, key=lambda x: x["size"])
        return sorted_edges

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
                if current_edge["vertex"].data.color == 'w':
                    current_edge["vertex"].data.color = 'g'
                    current_edge["vertex"].data.distance = current_vertex.distance + current_edge["size"]
                    current_edge["vertex"].data.predecessor = current_vertex
                    queue.put(current_edge["vertex"].data)
                current_edge = current_edge.next
            current_vertex.color = 'b'

    def dfs(self):
        pass

    def dfs_visit(self, vertex):
        pass

    def mst_kruskal(self):
        a = set()
        forest = []

        def make_set(vertex):
            return {vertex}
        
        def union(set_x, set_y):
            union = set_x.union(set_y)
            return union
        
        def find_set(x, foreest):
            for tree in forest:
                if x in tree:
                    return tree
        
        current_vertex = self.vertices_list.beginning

        while current_vertex is not None:
            new_tree = make_set(current_vertex.data.id)
            forest.append(new_tree)
            current_vertex = current_vertex.next

        sorted_edges = self.get_sorted_edges()

        for edge in sorted_edges:
            a_tree = find_set(edge["vertexa"])
            b_tree = find_set(edge["vertexb"])
            if a_tree != b_tree:
                ab_tree = a_tree.union(b_tree)
                forest.remove(a_tree)
                forest.remove(b_tree)
                forest.append(ab_tree)
                a = a.union(ab_tree)
        
        return a

    def mst_prim(self, weight, root):
        queue = Queue()
        current_vertex = self.vertices_list.beginning
        while current_vertex is not None:
            if current_vertex.data == root:
                current_vertex.data.key = 0
            else:
                current_vertex.data.key = float('inf')
            current_vertex.data.predecessor = None
            queue.put(current_vertex.data)
        while queue.empty() is False:
            pass


    def __str__(self):
        string = ""
        current_vertex = self.vertices_list.beginning
        while current_vertex is not None:
            string += f"{str(current_vertex.data)}"
            current_vertex = current_vertex.next
        return string
