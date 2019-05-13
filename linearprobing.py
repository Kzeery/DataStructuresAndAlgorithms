class Hashtable():
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size
    
    def hashfunction(self, key):
        return hash(key) % self.size

    def put(self, key, data):
        index = self.hashfunction(key)

        while self.keys[index]:
            if self.keys[index] == key:
                self.values[index] = data
                return
            
            index = (index+1)%self.size
        
        self.keys[index] = key
        self.values[index] = data
    
    def get(self, key):
        index = self.hashfunction(key)

        while self.keys[index]:
            if self.keys[index] == key:
                return self.values[index]
            
            index = (index+1)%self.size
        
        return None
