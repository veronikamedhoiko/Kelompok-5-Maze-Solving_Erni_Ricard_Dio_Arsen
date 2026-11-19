import unittest

from src.queue import Queue


class TestQueue(unittest.TestCase):

    def test_new_queue_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(len(queue), 0)

    def test_enqueue_dequeue_fifo(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 20)
        self.assertTrue(queue.is_empty())

    def test_peek_does_not_remove(self):
        queue = Queue()
        queue.enqueue("A")
        self.assertEqual(queue.peek(), "A")
        self.assertEqual(len(queue), 1)

    def test_empty_operations(self):
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.dequeue()
        with self.assertRaises(IndexError):
            queue.peek()

    def test_reuse_after_becoming_empty(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 2)


if __name__ == "__main__":
    unittest.main()
