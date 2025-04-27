from trees.binary_tree.binary_tree import BinaryTree
from trees.avl_tree.avl_node import AVLNode
# python -m trees.avl_tree.avl_tree

class AVLTree(BinaryTree):
    def __init__(self, node=None):
        super().__init__(node)

    def insert(self, node):
        if self.root == None:
            self.root = node
            return True
        current = self.root
        while True:
            if node.get_info() == current.get_info():
                return False
            elif node.get_info() < current.get_info():
                if current.get_left_child() is None:
                    current.set_left_child(node)
                    node.set_father(current)
                    self.balance()
                    return True  
                current = current.get_left_child()
            else:
                if current.get_right_child() is None:
                    current.set_right_child(node)
                    node.set_father(current)
                    self.balance()
                    return True 
                current = current.get_right_child()
    
    def delete(self, node):
        father = node.get_father()
        left_child = node.get_left_child()
        right_child = node.get_right_child()

        if left_child is not None and right_child is not None:
            sucessor = self.sucessor(node)
            sucessor_right_child = sucessor.get_right_child()
            self.delete(sucessor)
            sucessor.set_left_child(left_child)
            left_child.set_father(sucessor)
            node.set_left_child(None)

            if right_child != sucessor:
                sucessor.set_right_child(right_child)
                right_child.set_father(sucessor)
            else:
                sucessor.set_right_child(sucessor_right_child)
                sucessor_right_child.set_father(sucessor)       
            node.set_right_child(None)

            if father is None:
                self.root = sucessor
                sucessor.set_father(None)
            else:
                if node.is_left():
                    father.set_left_child(sucessor)
                else:
                    father.set_right_child(sucessor)
                sucessor.set_father(father)
            node.set_father(None)

        elif left_child is not None:
            if father is None:
                self.root = left_child
                left_child.set_father(None)
            else:
                if node.is_left():
                    father.set_left_child(left_child)
                else:
                    father.set_right_child(left_child)
                left_child.set_father(father)

            node.set_left_child(None)
            node.set_father(None)

        elif right_child is not None:
            if father is None:
                self.root = right_child
                right_child.set_father(None)
            else:
                if node.is_left():
                    father.set_left_child(right_child)
                else:
                    father.set_right_child(right_child)
                right_child.set_father(father)

            node.set_right_child(None)
            node.set_father(None)

        else:
            if father is None:
                self.root = None
            else:
                if node.is_left():
                    father.set_left_child(None)
                else:
                    father.set_right_child(None)

            node.set_father(None)

        
        self.update_balancing_factors()
        self.balance()

        return node

    def balance(self):
        while True:
            self.update_balancing_factors()
            pre_order = self.pre_order(self.root)
            balanced = True 
            for node in pre_order:
                if node.get_balancing_factor() >= 2 or node.get_balancing_factor() <= -2:
                    self.rotate(node)
                    balanced = False  
                    break
            if balanced:
                break  

    def calculate_height(self, node):
        if node is None:
            return 0
        left_height = self.calculate_height(node.get_left_child())
        right_height = self.calculate_height(node.get_right_child())
        return max(left_height, right_height) + 1

    def rotate(self, node):
        if node.get_balancing_factor() > 1:
            right_child = node.get_right_child()
            if right_child and right_child.get_balancing_factor() > 0:
                self.left_rotate(node)
            elif right_child and right_child.get_balancing_factor() < 0:
                self.right_rotate(right_child)
                self.left_rotate(node)
        elif node.get_balancing_factor() < -1:
            left_child = node.get_left_child()
            if left_child and left_child.get_balancing_factor() < 0:
                self.right_rotate(node)
            elif left_child and left_child.get_balancing_factor() > 0:
                self.left_rotate(left_child)
                self.right_rotate(node)
        
    def update_balancing_factors(self):
        post_order = self.post_order(self.root)
        for avl_node in post_order:
            left_child_height = self.calculate_height(
                avl_node.get_left_child())
            right_child_height = self.calculate_height(
                avl_node.get_right_child())
            avl_node.set_balancing_factor(
                right_child_height - left_child_height)
        pre_order = self.pre_order(self.root)
        return [f"{node.get_info()}: {node.get_balancing_factor()}" for node in pre_order]

    def left_rotate(self, node):
        node_right_child = node.get_right_child()
        node.set_right_child(node_right_child.get_left_child())
        if node_right_child.get_left_child() is not None:
            node_right_child.get_left_child().set_father(node)
        node_right_child.set_father(node.get_father())
        if node.get_father() is None:
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
        if node_left_child.get_right_child() is not None:
            node_left_child.get_right_child().set_father(node)
        node_left_child.set_father(node.get_father())
        if node.get_father() is None:
            self.root = node_left_child
        elif node.is_right():
            node.get_father().set_right_child(node_left_child)
        else:
            node.get_father().set_left_child(node_left_child)
        node_left_child.set_right_child(node)
        node.set_father(node_left_child)

    def repeated_numbers(self, list):
        rn = []
        for number in list:
            node = AVLNode(number)
            if not self.insert(node):
                rn.append(number)
        return rn
