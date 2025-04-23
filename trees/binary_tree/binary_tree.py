from binary_node import BinaryNode

class BinaryTree:
    def __init__(self, node=None):
        self.root = node
    
    def search(self, value):
        current = self.root
        while current.get_info() != value and current.get_info() is not None:
            if current.get_info() < value:
                current = current.get_right_child()
            else:
                current = current.get_left_child()
        return current

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
                    return True  
                current = current.get_left_child()
            else:
                if current.get_right_child() is None:
                    current.set_right_child(node)
                    node.set_father(current)
                    return True 
                current = current.get_right_child()

    def delete(self, node):
        father = node.get_father()
        left_child = node.get_left_child()
        right_child = node.get_right_child()

        if left_child is not None and right_child is not None:
            sucessor = self.sucessor(node)
            self.delete(sucessor)

            sucessor.set_left_child(left_child)
            left_child.set_father(sucessor)
            node.set_left_child()

            sucessor.set_right_child(right_child)
            right_child.set_father(sucessor)
            node.set_right_child()

            if father is None:
                self.root = sucessor
                sucessor.set_father(None)
            else:
                if node.is_left():
                    father.set_left_child(sucessor)
                else:
                    father.set_right_child(sucessor)
                sucessor.set_father(father)

            node.set_father()

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

            node.set_left_child()
            node.set_father()

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

            node.set_right_child()
            node.set_father()

        else:
            if father is None:
                self.root = None
            else:
                if node.is_left():
                    father.set_left_child()
                else:
                    father.set_right_child()

            node.set_father()

        return node

    def minimum(self, current=None):
        if current is None:
            current = self.root
        while current.get_left_child() is not None:
            current = current.get_left_child()
        return current

    def maximum(self, current=None):
        if current is None:
            current = self.root
        while current.get_right_child() is not None:
            current = current.get_right_child()
        return current

    def predecessor(self, node):
        if node.get_left_child() is not None:
            return self.maximum(node.get_left_child())
        current = node
        current_father = node.get_father()
        while current_father is not None and current == current_father.get_left_child():
            current = current_father
            current_father = current_father.get_father()
        return current_father

    def sucessor(self, node):
        if node.get_right_child() is not None:
            return self.minimum(node.get_right_child())
        current = node
        current_father = node.get_father()
        while current_father is not None and current == current_father.get_right_child():
            current = current_father
            current_father = current_father.get_father()
        return current_father

    def preorder(self, node, list=[]):
        if node is not None:
            list.append(node.get_info())
            self.preorder(node.get_left_child(), list)
            self.preorder(node.get_right_child(), list)
        return list
    
    def inorder(self, node, list=[]):
        if node is not None:
            self.inorder(node.get_left_child(), list)
            list.append(node.get_info())
            self.inorder(node.get_right_child(), list)
        return list
    
    def postorder(self, node, list=[]):
        if node is not None:
            self.postorder(node.get_left_child(), list)
            self.postorder(node.get_right_child(), list)
            list.append(node.get_info())
        return list

    def repeated_numbers(self, list):
        rn = []
        for number in list:
            node = BinaryNode(number)
            if not self.insert(node):
                rn.append(number)
        return rn
