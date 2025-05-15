class AL_Vertex:
    def __init__(self, id):
        self.id = str(id)
        self.color = None
        self.distance = None
        self.predecessor = None
    
    def __str__(self):
        return f"Id: {self.id}\nColor: {self.color}\nDistance: {self.distance}\nPredecessor: {self.predecessor}"
