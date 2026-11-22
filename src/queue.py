# ANGGOTA_03:
"""Implementasi Queue berbasis singly linked list."""

class _Node:
    """Node internal untuk Queue."""
    def _init_(self, value):
        self.value = value
        self.next = None
class Queue:
    """Queue dengan prinsip First In, First Out (FIFO)."""
    def _init_(self):
        self._front = None
        self._rear = None
        self._size = 0
    def enqueue(self, value):
        node = _Node(value)
        if self.is_empty():
            self._front = node
        else:
            self._rear.next = node
        self._rear = node
        self._size += 1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self._front.value
        self._front = self._front.next

 