from utils.dl_list import DL_List

class AL_Vertex:
    def __init__(self, id):
        self.id = str(id)
        self.edges = DL_List()
        self.color = None
        self.distance = None
        self.predecessor = None
        self.key = None
    
    def __str__(self):
        if self.edges.is_empty():
            return f"Node: {self.id}"
        string = f"Node: {self.id}, it edges:"
        current_edge = self.edges.beginning
        while current_edge is not None:
            string += f" {current_edge.data.id}"
            current_edge = current_edge.next
        return string
