# ANGGOTA_01:

import unittest
from src.linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    """Unit testing untuk Single Linked List."""

    def setUp(self):
        self.linked_list = SinglyLinkedList()

    def test_new_list_is_empty(self):
        self.assertTrue(self.linked_list.is_empty())
        self.assertEqual(len(self.linked_list), 0)
    def test_append(self):
        self.linked_list.append(10)
        self.linked_list.append(20)

        self.assertEqual(len(self.linked_list), 2)
        self.assertEqual(
            self.linked_list.display(),
            "10 -> 20 -> None"
        )
    def test_prepend(self):
        self.linked_list.append(20)
        self.linked_list.prepend(10)
        self.assertEqual(
            self.linked_list.display(),
            "10 -> 20 -> None"
        )
    def test_remove_first(self):
        self.linked_list.append(10)
        self.linked_list.append(20)

        result = self.linked_list.remove_first()
        self.assertEqual(result, 10)
        self.assertEqual(len(self.linked_list), 1)
    def test_peek(self):
        self.linked_list.append(10)
        self.assertEqual(self.linked_list.peek(), 10)
        self.assertEqual(len(self.linked_list), 1)
    def test_remove_first_empty(self):
        with self.assertRaises(IndexError):
            self.linked_list.remove_first()
    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            self.linked_list.peek()

if __name__ == "__main__":
    unittest.main()
