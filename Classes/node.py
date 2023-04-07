class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def val(self):
        return self.val
    
    def get_next(self):
        return self.next
    
    def set_next(self, node):
        self.next = node
        
