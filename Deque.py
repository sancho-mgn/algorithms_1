class _Node:
    def __init__(self, val):
        self.value = val
        self.head = None
        self.tail = None

class _DummyNode(_Node):
    def __init__(self):
        super().__init__(None)

class Deque:    
    def __init__(self):
        self.head = _DummyNode()
        self.tail = _DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def addFront(self, item):
        node = _Node(item)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.length += 1

    def addTail(self, item):
        node = _Node(item)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.length += 1

    def removeFront(self):
        if self.length:
            val = self.head.next.value
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self.length -= 1
            return val
        return None

    def removeTail(self):
        if self.length:
            val = self.tail.prev.value
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            self.length -= 1
            return val
        return None

    def size(self):
        return self.length