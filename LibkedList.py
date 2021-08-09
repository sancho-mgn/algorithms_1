class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        self.length += 1

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

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
		# check our linked list for a single value
                if self.head == node and self.tail == node:
                    self.head = None
                    self.tail = None
		# check our linked list if the length is greater than 2
                elif self.head != node and self.tail != node:
                    node_prev.next = node.next
                    node = node_prev
		# go through the nodes witg tails and delete until none
                elif self.tail == node:
                    self.tail = node_prev
                    node_prev.next = node.next
		# go through the nodes with heads and delete until none
                elif self.head == node:
                    self.head = node.next
                self.length -= 1
                if not all:
                    break
            node_prev = node
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
                self.tail = newNode
            self.head, newNode.next = newNode, self.head
            self.length += 1
        else:
            if self.head is not None:
                if self.tail == afterNode:
                    self.tail = newNode
                afterNode.next, newNode.next = newNode, afterNode.next
                self.length += 1