class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        self.count = 0

    def hash_encode(self, key):
        return sum(key.encode()) % self.size

    def put(self, key, value):
        i = self.hash_encode(key)
        least = min(self.hits)
        step = 3
        while step < self.size:
            if self.count == self.size:
                if self.hits[i] == least:
                    self.slots[i] = None
                    self.values[i] = None
                    self.hits[i] = 0
                    self.count -= 1
            if self.slots[i] is None:
                self.slots[i] = key
                self.values[i] = value
                self.hits[i] += 1
                self.count += 1
                break
            i += step-1
            if i > self.size-1:
                i = abs(i-self.size-1)
                step += 1
    
    def get(self, key):
        i = self.hash_encode(key)
        if self.slots[i] == key:
            self.hits[i] += 1
            return self.values[i]
        else:
            for i in range(self.size):
                if self.slots[i] == key:
                    self.hits[i] += 1
                    return self.values[i]
        return None