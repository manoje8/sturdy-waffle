## LFU - Least Frequent Used cache

class LFU:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
            self.freq = 1


    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def _add(self, node):
        temp = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = temp
        temp.prev = node


    def _delete(self, node):
        back = node.prev
        end = node.next

        back.next = end
        end.prev = back


    def _get(self, key):
        if key in self.cache:
            node = self.cache[key]
            node.freq += 1