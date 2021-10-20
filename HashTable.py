class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
    
    def hash_fun(self, value):
        return sum(value.encode()) % self.size

    def seek_slot(self, value):
        i = self.hash_fun(value)
        step = self.step
        while step < self.size:
            if self.slots[i] is None:
                return i
            i += step-1
            if i > self.size-1:
                i = abs(i-self.size-1)
                step += 1
        return None

    def put(self, value):
        i = self.seek_slot(value)
        if i is not None:
            self.slots[i] = value
            return i
        return None

    def find(self, value):
        i = self.hash_fun(value)
        step = self.step
        while step < self.size:
            if self.slots[i] == value:
                return i
            i += step-1
            if i > self.size-1:
                i = abs(i-self.size-1)
                step += 1
        return None