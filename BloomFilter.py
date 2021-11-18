class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.arr = 0

    def hash1(self, str1):
        i = 0
        for c in str1:
            i = (i*17 + ord(c)) % self.filter_len
        return 1 << i

    def hash2(self, str1):
        j = 0
        for c in str1:
            j = (j*223 + ord(c)) % self.filter_len
        return 1 << j

    def add(self, str1):
        if self.filter_len:
            self.arr = self.arr | self.hash1(str1) | self.hash2(str1)

    def is_value(self, str1):
        if self.filter_len and self.arr:
            mask = self.hash1(str1) | self.hash2(str1)
            return mask == self.arr & mask
        return False