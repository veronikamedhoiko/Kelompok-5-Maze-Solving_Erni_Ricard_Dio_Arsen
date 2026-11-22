# ANGGOTA_03:
import unittest
from src.queue import Queue

class TestQueue(unittest.TestCase):
    def test_new_queue_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        self.assertEqual(len(q), 0)
    def test_enqueue_dequeue_fifo(self):
        q = Queue()
        q.enqueue(10)
        q.enqueue(20)
        self.assertEqual(q.dequeue(), 10)
        self.assertEqual(q.dequeue(), 20)
        self.assertTrue(q.is_empty())
    def test_peek_does_not_remove(self):
        q = Queue()
        q.enqueue("A")
        self.assertEqual(q.peek(), "A")
        self.assertEqual(len(q), 1)
    def test_empty_operations(self):
        q = Queue()
        with self.assertRaises(IndexError):
            q.dequeue()
        with self.assertRaises(IndexError):
            q.peek()
    def test_reuse_after_becoming_empty(self):
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 2)
if __name__ == "__main__":
    unittest.main()