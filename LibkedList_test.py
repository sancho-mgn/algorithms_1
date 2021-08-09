from LinkedList import Node, LinkedList
from unittest import TestCase

class LinkedListTest(TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_find_all(self):
        n1 = Node(1)
        n1_1 = Node(1)
        n2 = Node(2)
        n5 = Node(5)
        
        self.list.add_in_tail(n1)
        self.list.add_in_tail(n2)
        self.list.add_in_tail(n1_1)
        self.list.add_in_tail(n5)

        # verify len list
        self.assertEqual(4, self.list.len())

        # verify finding all elements
        self.assertEqual([n1, n1_1], self.list.find_all(n1.value))

        # verify finding elements in empty list
        self.assertEqual([], self.list.find_all(LinkedList()))
        
        # vertify finding 1 element
        self.lst = LinkedList()
        n22 = Node(22)
        self.lst.add_in_tail(n22)
        self.assertEqual([n22], self.lst.find_all(n22.value))
    
    def test_delete(self):
        self.list.clean()
        n1 = Node(1)
        n1_2 = Node(1)
        n1_3 = Node(1)
        n2 = Node(2)
        n5 = Node(5)
        n1_4 = Node(1)
        n1_5 = Node(1)
        n999 = Node(999)
        n22 = Node(22)

        self.list.add_in_tail(n1)
        self.list.add_in_tail(n1_2)
        self.list.add_in_tail(n1_3)
        self.list.add_in_tail(n2)
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(n5)
        self.list.add_in_tail(n1_4)
        self.list.add_in_tail(n1_5)
        self.list.add_in_tail(n999)
        self.list.add_in_tail(n22)

        # check len list
        self.assertEqual(10, self.list.len())

        # check delete, all=False
        self.list.delete(22)
        self.assertEqual(9, self.list.len())

        # check tail
        obj = self.list.find(n999.value)
        self.assertEqual(self.list.tail, obj)
        
        # check delete, all=True
        self.list.delete(1, all=True)
        self.assertEqual(3, self.list.len())

        # check head
        head = self.list.head
        self.assertEqual(head, self.list.find(n2.value))

        # check tail
        tail = self.list.tail
        self.assertEqual(tail, n999)

        # check delete all elements
        self.list.delete(n2.value)
        self.assertEqual(self.list.head, n5)
        self.assertEqual(self.list.tail, n999)

        self.list.delete(n999.value)
        self.assertEqual(self.list.head, n5)
        self.assertEqual(self.list.tail, n5)

        self.list.delete(n5.value)
        self.assertEqual(None, self.list.head)
        self.assertEqual(None, self.list.tail)

    def test_insert(self):
        self.list.clean()

        n1 = Node(1)
        n1_1 = Node(1)
        n2 = Node(2)
        n5 = Node(5)

        self.list.add_in_tail(n1)
        self.list.add_in_tail(n2)
        self.list.add_in_tail(n1_1)
        self.list.add_in_tail(n5)

        # check list len
        self.assertEqual(4, self.list.len())

        # check insert
        n55 = Node(55)
        self.list.insert(n1, n55)
        self.assertEqual(n55, self.list.find(n55.value))
        n55_obj = self.list.find(n55.value)
        self.assertEqual(n55, n1.next)
        
        # check head
        self.assertEqual(n1, self.list.head)

        # check tail
        self.assertEqual(n5, self.list.tail)

        # check insert None
        n111 = Node(111)
        self.list.insert(None, n111)
        
        # check head
        self.assertEqual(n111, self.list.head)

        # check tail
        self.assertEqual(n5, self.list.tail)

        # check next
        n111_obj = self.list.find(n111.value)
        self.assertEqual(n1, n111_obj.next)

    def test_empty(self):
        self.list = LinkedList()
        n55 = Node(55)
        self.list.insert(None, n55)
        self.assertEqual(self.list.head, self.list.find(n55.value))

        self.list.clean()

        self.list.insert(Node(1), Node(55))
        self.assertEqual(None, self.list.head)
        self.assertEqual(None, self.list.tail)
        
        # check insert in empty list with afterNode=None
        self.list.clean()
        n1 = Node(1)
        self.list.insert(None, n1)

        # check head and tail
        self.assertEqual(n1, self.list.head)
        self.assertEqual(n1, self.list.tail)
        
        # check insert in empty list with afterNode!=None
        self.list.clean()
        self.list.insert(Node(1), n1)

        self.assertEqual(None, self.list.head)
        self.assertEqual(None, self.list.tail)

        # check find in empty list
        self.assertEqual(None, self.list.find(Node(1)))

        # check find_all in empty list
        self.assertEqual([], self.list.find_all(Node(1)))

        # check delete in empty list
        self.assertEqual(self.list.head, self.list.delete(1))
        self.assertEqual(self.list.tail, self.list.delete(1))

        # check clean in empty list
        self.list.clean()
        self.assertEqual(None, self.list.head)
        self.assertEqual(None, self.list.tail)

        # check len in empty list
        self.assertEqual(0, self.list.len())

    def test_one(self):
        self.list.clean()
        n1 = Node(1)
        self.list.add_in_tail(n1)
        
        # check find all
        self.assertEqual([n1], self.list.find_all(n1.value))
        self.assertEqual([], self.list.find_all(Node(19).value))

        # check delete, all=False
        self.list.delete(Node(1).value)
        self.assertEqual(self.list.head, None)
        self.assertEqual(self.list.tail, None)

        # check delete, all=True
        self.list.add_in_tail(n1)
        self.list.delete(Node(1).value, all=True)
        self.assertEqual(self.list.head, None)
        self.assertEqual(self.list.tail, None)

        # check insert after None
        self.list.add_in_tail(n1)
        n10 = Node(10)
        self.list.insert(None, n10)
        self.assertEqual(n10, self.list.head)
        self.assertEqual(n1, self.list.tail)

        # check insert after some node in the middle of the list
        n12 = Node(12)
        self.list.insert(n10, n12)
        self.assertEqual(n10, self.list.head)
        self.assertEqual(n1, self.list.tail)

        # check insert after end node
        n13 = Node(13)
        self.list.insert(n1, n13)
        self.assertEqual(n10, self.list.head)
        self.assertEqual(n13, self.list.tail)

    def test_few(self):
        pass