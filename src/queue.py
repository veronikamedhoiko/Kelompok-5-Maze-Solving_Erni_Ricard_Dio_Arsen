"""Implementasi Queue berbasis singly linked list."""

class _Node:
    """Node internal untuk Queue."""

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """Queue dengan prinsip First In, First Out (FIFO)."""

    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def enqueue(self, value):
        """Menambahkan elemen ke belakang Queue."""
        node = _Node(value)
        if self.is_empty():
            self._front = node
        else:
            self._rear.next = node
        self._rear = node
        self._size += 1

    def dequeue(self):
        """Menghapus dan mengembalikan elemen paling depan."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self._front.value
        self._front = self._front.next
        self._size -= 1
        if self._front is None:
            self._rear = None
        return value

    def peek(self):
        """Mengembalikan elemen depan tanpa menghapusnya."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._front.value

    def is_empty(self):
        """Memeriksa apakah Queue kosong."""
        return self._size == 0

    def __len__(self):
        return self._size
