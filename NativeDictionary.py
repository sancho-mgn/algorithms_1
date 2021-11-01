class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        return sum(key.encode()) % self.size

    def is_key(self, key):
        i = self.hash_fun(key)
        if i < self.size:
            if self.slots[i] == key:
                return True
        return False

    def put(self, key, value):
        i = self.hash_fun(key)
        step = 3
        while step < self.size:
            if self.slots[i] is None:
                self.slots[i] = key
                self.values[i] = value
                break
            i += step-1
            if i > self.size-1:
                i = abs(i-self.size-1)
                step += 1

    def get(self, key):
        if self.is_key(key):
            return self.values[self.hash_fun(key)]
        return None