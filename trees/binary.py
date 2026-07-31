from trees.BNode import BNode
from collections import deque


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert(self, node, value):
        if node is None:
            return BNode(value)

        elif value <= node.data:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        return node

    def add(self, value):
        self.root = self._insert(self.root, value)

    def search(self, node, target) -> bool:
        if node is None:
            return False
        elif node.data == target:
            return True
        elif target <= node.data:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)

    def find_min(self):
        temp = self.root

        if temp is None:
            print("ERROR: Binary Tree is empty")
            return False

        while temp.left is not None:
            temp = temp.left
        return temp.data

    def find_max(self):
        temp = self.root

        if temp is None:
            print("ERROR: Binary Tree is empty")
            return False

        while temp.right is not None:
            temp = temp.right
        return temp.data

    def find_height(self, node):
        temp = node
        if temp is None:
            return False

        return max(self.find_height(node.left), self.find_height(node.right)) + 1

    def level_order(self):
        temp = self.root

        if temp is None:
            return

        q = deque([temp])

        while len(q) != 0:
            curr = q.popleft()
            print(curr.data, end="->")

            if curr.left is not None:
                q.append(curr.left)

            if curr.right is not None:
                q.append(curr.right)

    def pre_order(self, node):
        """
        <root><left><right>
        :param node:
        :return:
        """
        temp = node
        if temp is None:
            return

        print(temp.data, end="->")
        self.pre_order(temp.left)
        self.pre_order(temp.right)

    def in_order(self, node):
        """
        <left><root><right>
        :param node:
        :return:
        """
        temp = node
        if temp is None:
            return

        self.pre_order(temp.left)
        print(temp.data, end="->")
        self.pre_order(temp.right)

    def post_order(self, node):
        """
        <left><right><root>
        :param node:
        :return:
        """
        temp = node
        if temp is None:
            return

        self.pre_order(temp.left)
        self.pre_order(temp.right)
        print(temp.data, end="->")


if __name__ == "__main__":
    bst = BinarySearchTree()
    arr = [5, 8, 6, 2, 3, 7]
    for val in arr:
        bst.add(val)

    print(bst.search(bst.root, 9))
    print(bst.find_min())
    print(bst.find_max())
    print(bst.find_height(bst.root))
    bst.level_order()
    print()
    bst.pre_order(bst.root)
    print()
    bst.in_order(bst.root)
    print()
    bst.post_order(bst.root)
