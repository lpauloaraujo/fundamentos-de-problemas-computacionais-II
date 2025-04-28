from trees.avl_tree.avl_tree import AVLTree
from trees.rb_tree.rb_node import RBNode

class RBTree(AVLTree):
    def __init__(self, node=None):
        self.none = RBNode("b")
        self.root = node
    
    def insert(self, node):
        if self.root == None:
            self.root = node
            self.root.set_color('b')
            self.root.set_father(self.none)
            self.set_children_to_none(self.root)
            return True
        current = self.root
        while True:
            node.set_color('r')
            if node.get_info() == current.get_info():
                self.rb_insert_fixup(self, node)
                return False
            elif node.get_info() < current.get_info():
                if current.get_left_child() is None:
                    current.set_left_child(node)
                    node.set_father(current)
                    self.set_children_to_none(node)
                    self.rb_insert_fixup(self, node)
                    return True  
                current = current.get_left_child()
            else:
                if current.get_right_child() is None:
                    current.set_right_child(node)
                    node.set_father(current)
                    self.set_children_to_none(node)
                    self.rb_insert_fixup(self, node)
                    return True 
                current = current.get_right_child()
    
    def rb_insert_fixup(self, node):
        pass

    def set_children_to_none(self, node):
        node.set_left_child(self.none)
        node.set_right_child(self.none)
