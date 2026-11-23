# ANGGOTA_02:

import unittest
from src.stack import Stack

class TestStack(unittest.TestCase):
    """Pengujian fungsi Stack."""
    def test_new_stack_is_empty(self):
        stack = Stack()

        self.assertTrue(stack.is_empty())
        self.assertEqual(len(stack), 0)
    def test_push_pop_lifo(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)

        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.is_empty())
    def test_peek_does_not_remove(self):
        stack = Stack()
        stack.push("A")

        self.assertEqual(stack.peek(), "A")
        self.assertEqual(len(stack), 1)
    def test_empty_pop_and_peek(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()

if __name__ == "__main__":
    unittest.main()