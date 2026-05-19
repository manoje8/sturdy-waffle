"""
Least Recent Used (LRU) cache


Real-world caching problem
Combines HashMap with Doubly LinkedList
Tests O(1) operation design

Add right after head (most recent)
Delete right before tail (least used)
"""


class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        previous = node.prev
        nxt = node.next

        previous.next = nxt
        nxt.prev = previous

    def _add(self, node):
        old = self.head.next

        # updating new node
        node.next = old
        node.prev = self.head

        # update prev one
        old.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]

            self._remove(node)
            self._add(node)

            return node.value

        return -1

    def put(self, key, value):

        if key in self.cache:
            self._remove(self.cache[key])

        node = self.Node(key, value)
        self._add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.tail.prev

            self._remove(lru)
            del self.cache[lru.key]
