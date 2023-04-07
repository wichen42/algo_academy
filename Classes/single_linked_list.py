from node import *

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, node):
        new_node = node;
        new_node.set_next(self.head)
        self.head = new_node
        
    def size(self):
        current = self.head
        counter = 0
        while current:
            counter+=1
            current = current.get_next()
        return counter
    
    def search(self, target):
        current = self.head
        found = False
        while current and found is False:
            if current.val() == target:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Target is not in the list")
        return current
    
    def delete(self, target):
        current = self.head
        found = False
        while current and found is False:
            if current.val() == target:
                found = True
            else:
                prev = current
                current = current.get_next()
        if current is None:
            self.head = current.get_next()
        else: 
            prev.set_next(current.get_next())

