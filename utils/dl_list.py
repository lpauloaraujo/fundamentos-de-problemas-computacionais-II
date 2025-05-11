class DLL_Node():
    def __init__(self, data) -> None:
        self.data = data
        self.previous = None
        self.next = None

class DL_List():
    def __init__(self) -> None:
        self.beginning = None
        self.ending = None
    
    def is_empty(self):
        return self.beginning == None or self.ending == None
    
    def insert_at_ending(self, data):
        new_node = DLL_Node(data)
        if self.is_empty():
            self.beginning = self.ending = new_node
        else:
            self.ending.next = new_node
            new_node.previous = self.ending
            self.ending = new_node
    
    def insert_at_beggining(self, data):
        new_node = DLL_Node(data)
        if self.is_empty():
            self.beginning = self.ending = new_node
        else:
            new_node.next = self.beginning
            self.beginning.previous = new_node
            self.beginning = new_node

    def search(self, node_value):
        current_node = self.beginning
        while current_node is not None:
            if current_node.data == node_value:
                return current_node
            current_node = current_node.next
        return None
    
    def remove(self, node_value):
        removed_node = self.search(node_value)
        if removed_node == None:
            return None
        elif removed_node == self.beginning == self.ending:
            self.beginning = self.ending = None
            return removed_node
        if removed_node == self.ending:
            penultimate = self.ending.previous
            penultimate.next = None
            self.ending = penultimate
            return removed_node
        previous = removed_node.previous
        next = removed_node.next
        previous.next = next
        next.previous = previous
        return removed_node
    
    def __str__(self) -> str:
        string = ""
        current_node = self.beginning
        while current_node is not None:
            string += f"{current_node.data}"
            current_node = current_node.next
        return string
