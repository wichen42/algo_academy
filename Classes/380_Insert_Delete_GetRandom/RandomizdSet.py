class RandomizedSet:
    
    def __init__(self):
        self.map = {}
        self.list = []
        
    def insert(self, val):
       if val in self.map:
           return False
       
       self.list.append(val) 
       self.map[val] = len(self.list)-1
       return True
        
    def remove(self, val):
        if val not in self.map:
            return False
        
        lastElement = self.list[-1]
        idx = self.map[val]
        
        self.list[idx], self.map[lastElement] = lastElement, idx
        self.list.pop()
        del self.map[val]
        return True

    def getRandom(self):
        return random.choice(self.list)        