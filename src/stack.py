"""Implementasi Stack berbasis singly linked list."""

class _Node:
    """Node internal untuk Stack."""

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """Stack dengan prinsip Last In, First Out (LIFO)."""

    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, value):
        """Menambahkan elemen ke bagian atas Stack."""
        node = _Node(value)
        node.next = self._top
        self._top = node
        self._size += 1

    def pop(self):
        """Menghapus dan mengembalikan elemen teratas."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return value

    def peek(self):
        """Mengembalikan elemen teratas tanpa menghapusnya."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._top.value

    def is_empty(self):
        """Memeriksa apakah Stack kosong."""
        return self._size == 0

    def __len__(self):
        return self._size
