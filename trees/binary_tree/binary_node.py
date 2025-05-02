class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.father = None
        self.left_child = None
        self.right_child = None
        
    def set_father(self, node=None):
        self.father = node
    
    def set_left_child(self, node=None):
        self.left_child = node
    
    def set_right_child(self, node=None):
        self.right_child = node
    
    def get_info(self):
        return self.value
    
    def get_father(self):
        return self.father
    
    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child
    
    def is_left(self):
        if self.father.get_left_child() == self:
            return True
        else:
            return False

    def is_right(self):
        if self.father.get_right_child() == self:
            return True
        else:
            return False
    
    def brother(self):
        if self.is_left:
            return self.father.get_right_child()
        elif self.is_right:
            return self.father.get_left_child()
