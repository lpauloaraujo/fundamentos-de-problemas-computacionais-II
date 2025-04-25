from ..binary_tree.binary_tree import BinaryTree
from .avl_node import AVLNode

class AVLTree(BinaryTree):
    def __init__(self, node=None):
        super().__init__(node)
    
    def calculate_height(self, node):
        if node is None:
            return 0
        left_height = self.calculate_height(node.get_left_child())
        right_height = self.calculate_height(node.get_right_child())
        return max(left_height, right_height) + 1

    def update_balancing_factors(self):
        post_order = self.post_order(self.root)
        for avl_node in post_order:
            left_child_height = self.calculate_height(avl_node.get_left_child())
            right_child_height = self.calculate_height(avl_node.get_right_child())
            avl_node.set_balancing_factor(right_child_height - left_child_height)
        return [f"{avl_node.get_info()}: {avl_node.get_balancing_factor()}" for avl_node in post_order]
    
    def repeated_numbers(self, list):
        rn = []
        for number in list:
            node = AVLNode(number)
            if not self.insert(node):
                rn.append(number)
        return rn
