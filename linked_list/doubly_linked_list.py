from linked_list.list import List


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        node = List(val)

        node.prev = self.head

        if self.head is not None:
            node.next = self.head

        self.head = node

    def print_out(self):
        node = self.head

        while node:
            print(node.value, end=", ")
            node = node.next

        print("\n")
