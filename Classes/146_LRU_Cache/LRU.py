class LRUCache:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.DLL = new DoublyLinkedList()
        self.hash = {}
        
    def get(self, key):
        if key not in self.hash:
            return -1
        
        self.DLL.remove(self.hash[key])
        self.hash[key] = self.DLL.push(self.hash[key])
        
        return self.hash[key].val
    
    def put(self, key, val):
        if key in self.hash:
            self.DLL.remove(self.hash[key])
            
        newNode = Node(key,val)
        self.hash[key] = self.DLL.push(newNode)
        
        if self.DLL.length > self.capacity:
            lru = self.DLL.head.next
            del self.hash[lru.key]
            self.DLL.remove(lru)

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DobulyLinkedList:
    
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        
        self.head.prev = self.tail
        self.tail.next = self.head
        
        self.length = 0
        
    def remove(self, node):
        prv = node.prev
        nxt = node.next
        
        prv.next = node
        nxt.prv = node
        
        node.next = nxt
        node.prev = prv
        
        self.length -= 1
        
        return node
    
    def push(self, node):
        prv = self.tail.prev
        nxt = self.tail
        
        prv.next = nxt
        node.prev = prv
        
        self.length += 1
        
        return node
        