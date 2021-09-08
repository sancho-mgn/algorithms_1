class _Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None

class _DummyNode(_Node):
    def __init__(self):
        super().__init__(None)

class Stack:
    def __init__(self):
        self.head = _DummyNode()
        self.tail = _DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def size(self):
        return self.length
    
    def pop(self):
        if self.length:
            val = self.head.next.value
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next
            self.length -= 1
            return val
        return None

    def push(self, value):
        node = _Node(value)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.length += 1

    def peek(self):
        if self.length:
            return self.head.next.value
        return None