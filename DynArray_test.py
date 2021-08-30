from DynArray import DynArray
from unittest import TestCase

class DynArrayTest(TestCase):
    
    def setUp(self):
        self.array = DynArray()

    def test_insert(self):
        # test with empty array
        # self.array.insert(0, 1) -> IndexError 
        
        # test with one element
        self.array.append(1) # -> [1]
        self.array.insert(0, 5) # -> [5, 1]
        self.assertEqual(2, self.array.__len__())
        self.assertEqual(1, self.array[1])
        self.assertEqual(5, self.array[0])
        
        self.array.insert(1, 2) # -> [5, 2, 1]
        self.assertEqual(3, self.array.__len__())
        self.assertEqual(5, self.array[0])
        self.assertEqual(2, self.array[1])
        self.assertEqual(1, self.array[2])

        self.array.insert(2, 3) # -> [5, 2, 3, 1]
        self.assertEqual(4, self.array.__len__())
        self.assertEqual(3, self.array[2])
        self.assertEqual(1, self.array[3])
        

        # testing reallocation
        for i in range(12):
            self.array.append(i)
        
        self.assertEqual(16, self.array.__len__())
        self.array.append(11)
        self.assertEqual(32, self.array.capacity)

    def test_insert1(self):
        self.assertEqual(0, self.array.__len__())
        self.array.append(1)
        self.assertEqual(1, self.array.__len__())
        
        self.array.insert(1, 22)
        self.assertEqual(2, self.array.__len__())
        self.assertEqual(22, self.array[1])

    def test_delete(self):
        self.array.append(1)
        self.array.append(2) # -> [1, 2]
        self.assertEqual(2, self.array.__len__())
        self.assertEqual(2, self.array[1])
        self.assertEqual(1, self.array[0])

        self.array.delete(0) # -> [2] capacity = 16
        self.assertEqual(1, self.array.__len__())
        self.assertEqual(2, self.array[0])

        self.array.append(3) # -> [2, 3]
        self.array.append(4) # -> [2, 3, 4]

        self.array.delete(2) # -> [2, 3]
        self.assertEqual(2, self.array.__len__())
        self.assertEqual(3, self.array[1])
        self.assertEqual(2, self.array[0])

        self.array.append(5) # -> [2, 3, 5]
        self.array.delete(1) # -> [2, 5]
        self.assertEqual(2, self.array.__len__())
        self.assertEqual(2, self.array[0])
        self.assertEqual(5, self.array[1])

    def test_insert2(self):
        self.array.append(1)
        self.array.insert(0, 12)
        
        # check len
        self.assertEqual(2, self.array.__len__())
        
        # check capacity
        self.assertEqual(16, self.array.capacity)

        # insert new elements for length(array) = 16
        for i in range(14):
            self.array.insert(i, i)
        
        # check len array
        self.assertEqual(16, self.array.__len__())

        # insert new 17th element
        self.array.insert(0, 55)

        # check new capacity value
        self.assertEqual(32, self.array.capacity)
        
        # check inserting new elements to index = count (array)
        self.array.insert(17, 2)
        
        num = self.array[1]
        self.array.delete(0)

        self.assertEqual(17, self.array.__len__())

        self.assertEqual(num, self.array[0])
        
        # delete some elements
        self.array.delete(0) # len -> 16
        self.assertEqual(32, self.array.capacity)

        self.array.delete(0) # len -> 15
        self.assertEqual(21, self.array.capacity)
        self.assertEqual(15, self.array.__len__())

        # delete element in the wrong position
        # self.array.delete(-1)
        # self.array.delete(15)

        # test min capcity after deleting few elements
        for i in range(5):
            self.array.delete(0)

        self.assertEqual(10, self.array.__len__())
        self.assertEqual(16, self.array.capacity) # capacity does not equal 14!