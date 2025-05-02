from trees.avl_tree.avl_tree import AVLTree
from trees.rb_tree.rb_node import RBNode

class RBTree(AVLTree):
    def __init__(self, node=None):
        self.none = RBNode()
        self.none.set_color('b')
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
                return False
            elif node.get_info() < current.get_info():
                if current.get_left_child() == self.none:
                    current.set_left_child(node)
                    node.set_father(current)
                    self.set_children_to_none(node)
                    self.rb_insert_fixup(node)
                    return True
                current = current.get_left_child()
            else:
                if current.get_right_child() == self.none:
                    current.set_right_child(node)
                    node.set_father(current)
                    self.set_children_to_none(node)
                    self.rb_insert_fixup(node)
                    return True
                current = current.get_right_child()
    
    def rb_insert_fixup(self, node):
        while node.get_father().get_color() == 'r':
            if node.get_father().is_left():
                node_uncle = node.get_father().get_father().get_right_child()
                if node_uncle.get_color() == 'r':
                    node.get_father().set_color('b') 
                    node_uncle.set_color('b') 
                    node.get_father().get_father().set_color('r') 
                    node = node.get_father().get_father()
                else:
                    if node.is_right():
                        node = node.get_father()
                        self.left_rotate(node)
                    node.get_father().set_color('b')
                    node.get_father().get_father().set_color('r')
                    self.right_rotate(node.get_father().get_father())
            else:
                node_uncle = node.get_father().get_father().get_left_child()
                if node_uncle.get_color() == 'r':
                    node.get_father().set_color('b') 
                    node_uncle.set_color('b') 
                    node.get_father().get_father().set_color('r') 
                    node = node.get_father().get_father()
                else:
                    if node.is_left():
                        node = node.get_father()
                        self.right_rotate(node)
                    node.get_father().set_color('b')
                    node.get_father().get_father().set_color('r')
                    self.left_rotate(node.get_father().get_father())
        self.root.set_color('b')

    def set_children_to_none(self, node):
        node.set_left_child(self.none)
        node.set_right_child(self.none)

    def left_rotate(self, node):
        node_right_child = node.get_right_child()
        node.set_right_child(node_right_child.get_left_child())
        if node_right_child.get_left_child() is not self.none:
            node_right_child.get_left_child().set_father(node)
        node_right_child.set_father(node.get_father())
        if node.get_father() is self.none:
            self.root = node_right_child
        elif node.is_left():
            node.get_father().set_left_child(node_right_child)
        else:
            node.get_father().set_right_child(node_right_child)
        node_right_child.set_left_child(node)
        node.set_father(node_right_child)

    def right_rotate(self, node):
        node_left_child = node.get_left_child()
        node.set_left_child(node_left_child.get_right_child())
        if node_left_child.get_right_child() is not self.none:
            node_left_child.get_right_child().set_father(node)
        node_left_child.set_father(node.get_father())
        if node.get_father() is self.none:
            self.root = node_left_child
        elif node.is_right():
            node.get_father().set_right_child(node_left_child)
        else:
            node.get_father().set_left_child(node_left_child)
        node_left_child.set_right_child(node)
        node.set_father(node_left_child)

    def pre_order(self, node, list=None):
        if list is None: 
            list = []
        if node is not self.none:
            list.append(node)
            self.pre_order(node.get_left_child(), list)
            self.pre_order(node.get_right_child(), list)
        return list
    
    def in_order(self, node, list=None):
        if list is None: 
            list = []
        if node is not self.none:
            self.in_order(node.get_left_child(), list)
            list.append(node)
            self.in_order(node.get_right_child(), list)
        return list
    
    def post_order(self, node, list=None):
        if list is None: 
            list = []
        if node is not self.none:
            self.post_order(node.get_left_child(), list)
            self.post_order(node.get_right_child(), list)
            list.append(node)
        return list

    def delete(self, node):
        left_child = node.get_left_child()
        right_child = node.get_right_child()

        if left_child is self.none or right_child is self.none:
            y = node
        else:
            y = self.sucessor(node)
        if y.get_left_child() is not self.none:
            x = y.get_left_child()
        else:
            x = y.get_right_child()
        x.set_father(y.get_father())
        if y.get_father() is self.none:
            self.root = x
        else:
            if y.is_left():
                y.get_father().set_left_child(x)
            else:
                y.get_father().set_right_child(x)
        if y != node:
            node.set_info(y.get_info())
        if y.get_color() == 'b':
            self.rb_delete_fixup(x)
        return y
    
    def rb_delete_fixup(self, node):
        while node is not self.root and node.get_color() == 'b':
            if node.is_left():
                brother = node.brother()
                if brother.get_color() == 'r':
                    brother.set_color('b')
                    node.get_father().set_color('r')
                    self.left_rotate(node.get_father())
                    brother = node.get_father().right_child()
                if brother.get_left_child().get_color() == 'b' and brother.get_right_child().get_color() == 'b':
                    brother.set_color('r')
                    node = node.get_father()
                else:
                    if brother.get_right_child().get_color() == 'b':
                        brother.get_left_child().set_color('b')
                        brother.set_color('r')
                        self.right_rotate(brother)
                        brother = node.get_father().get_right_child()
                    brother.set_color(node.get_father().get_color())
                    node.get_father().set_color('b')
                    brother.get_right_child().get_color('b')
                    self.left_rotate(node.get_father())
                    node = self.root
            else:
                brother = node.brother()
                if brother.get_color() == 'r':
                    brother.set_color('b')
                    node.get_father().set_color('r')
                    self.right_rotate(node.get_father())
                    brother = node.get_father().left_child()
                if brother.get_right_child().get_color() == 'b' and brother.get_left_child().get_color() == 'b':
                    brother.set_color('r')
                    node = node.get_father()
                else:
                    if brother.get_left_child().get_color() == 'b':
                        brother.get_right_child().set_color('b')
                        brother.set_color('r')
                        self.left_rotate(brother)
                        brother = node.get_father().get_left_child()
                    brother.set_color(node.get_father().get_color())
                    node.get_father().set_color('b')
                    brother.get_left_child().get_color('b')
                    self.right_rotate(node.get_father())
                    node = self.root
            node.set_color('b')

    def minimum(self, current=None):
        if current is self.none:
            current = self.root
        while current.get_left_child() is not self.none:
            current = current.get_left_child()
        return current

    def maximum(self, current=None):
        if current is self.none:
            current = self.root
        while current.get_right_child() is not self.none:
            current = current.get_right_child()
        return current

    def predecessor(self, node):
        if node.get_left_child() is not self.none:
            return self.maximum(node.get_left_child())
        current = node
        current_father = node.get_father()
        while current_father is not self.none and current == current_father.get_left_child():
            current = current_father
            current_father = current_father.get_father()
        return current_father

    def sucessor(self, node):
        if node.get_right_child() is not self.none:
            return self.minimum(node.get_right_child())
        current = node
        current_father = node.get_father()
        while current_father is not self.none and current == current_father.get_right_child():
            current = current_father
            current_father = current_father.get_father()
        return current_father
