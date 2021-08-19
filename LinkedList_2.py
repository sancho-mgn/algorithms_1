class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
        self.length += 1

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        nodes = list()
        node = self.head
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if node == self.head and node == self.tail:
                    self.head = None
                    self.tail = None
                elif node != self.head and node != self.tail:
                    node.prev.next, node.next.prev = node.next, node.prev
                elif node == self.tail:
                    self.tail = node.prev
                    node.prev.next = node.next
                elif node == self.head:
                    self.head = node.next
                    node.next.prev = node.prev
                self.length -= 1
                if not all:
                    break
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None
        self.length = 0

    def len(self):
        return self.length

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                newNode.prev = None
                newNode.next = None
                self.head = newNode
            else:
                newNode.next = self.tail.next
                self.tail.next, newNode.prev = newNode, self.tail
            self.tail = newNode
            self.length += 1
        else:
            if self.head is not None:
                if self.tail == afterNode:
                    self.tail = newNode
                afterNode.next, newNode.next = newNode, afterNode.next
                newNode.prev = afterNode
                self.length += 1

    def add_in_head(self, newNode):
        if self.head is not None:
            self.head.prev = newNode
        else:
            self.tail = newNode
        newNode.next = self.head
        self.head = newNode
        self.length += 1