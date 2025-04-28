from trees.binary_tree.binary_node import BinaryNode

class RBNode(BinaryNode):
    def __init__(self, value):
        super().__init__(value)
        self.color = None
    
    def set_color(self, color):
        if color not in 'rb':
            print("As opções de cores são apenas 'r' ou 'b'.")
        else:
            self.color = color

    def get_color(self):
        return self.color
