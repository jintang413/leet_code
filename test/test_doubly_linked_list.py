import unittest
from list.doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def test_delete_at_index(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_add_at_index(self):
        l = DoublyLinkedList()
        expect_list = [1, 3, 4]
        l.addAtIndex(0, 1)
        l.addAtIndex(1, 4)
        l.addAtIndex(1, 3)
        self.assertListEqual(l.tolist(), expect_list)
        expect_list.reverse()
        self.assertListEqual(l.tolist(reverse=True), expect_list)


if __name__ == '__main__':
    unittest.main()
