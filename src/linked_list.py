# ANGGOTA_01:

class Node:
    """Merepresentasikan satu Node."""
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    """Implementasi struktur data Single Linked List."""
    def __init__(self):
        self.head = None
        self.size = 0
    def is_empty(self):
        return self.head is None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self.size += 1
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    def remove_first(self):
        if self.is_empty():
            raise IndexError("Linked List kosong")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    def peek(self):
        if self.is_empty():
            raise IndexError("Linked List kosong")
        return self.head.data
    def __len__(self):
        return self.size
    def display(self):
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + " -> "
            current = current.next
        return result + "None"