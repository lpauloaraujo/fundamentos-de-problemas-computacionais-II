from ..binary_tree.binary_node import BinaryNode

class AVLNode(BinaryNode):
    def __init__(self, value):
        super().__init__(value)
        self.balancing_factor = None

    def set_balancing_factor(self, value):
        self.balancing_factor = value

    def get_balancing_factor(self):
        return self.balancing_factor
