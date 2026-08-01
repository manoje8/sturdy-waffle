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

    def find_min(self, node):
        temp = node

        if temp is None:
            raise ValueError("Cannot find min of an empty subtree")

        while temp.left is not None:
            temp = temp.left
        return temp.data

    def find_max(self, node):
        temp = node

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

        self.in_order(temp.left)
        print(temp.data, end="->")
        self.in_order(temp.right)

    def post_order(self, node):
        """
        <left><right><root>
        :param node:
        :return:
        """
        temp = node
        if temp is None:
            return

        self.post_order(temp.left)
        self.post_order(temp.right)
        print(temp.data, end="->")

    def delete(self, value):
        self.root = self._delete_node(self.root, value)

    def _delete_node(self, node, value):
        if node is None:
            return node
        elif value < node.data:
            node.left = self._delete_node(node.left, value)
        elif value > node.data:
            node.right = self._delete_node(node.right, value)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                temp = self.find_min(node.right)
                node.data = temp
                node.right = self._delete_node(node.right, temp)

        return node

    def isBST(self) -> bool:
        node = self.root
        return self.is_binary_search_tree(node, float("-inf"), float("inf"))

    def is_binary_search_tree(self, node, min_val, max_val):
        if node is None:
            return True

        if (
            node.data > min_val
            and node.data < max_val
            and self.is_binary_search_tree(node.left, min_val, node.data)
            and self.is_binary_search_tree(node.right, node.data, max_val)
        ):
            return True
        else:
            return False


if __name__ == "__main__":
    bst = BinarySearchTree()
    arr = [5, 8, 6, 2, 3, 7]
    for val in arr:
        bst.add(val)

    print(bst.search(bst.root, 9))
    print(bst.find_min(bst.root))
    print(bst.find_max(bst.root))
    print(bst.find_height(bst.root))
    bst.level_order()
    print()
    bst.pre_order(bst.root)
    print()
    bst.in_order(bst.root)
    print()
    bst.post_order(bst.root)
    print()
    bst.delete(5)
    bst.level_order()
    print()
    print(bst.isBST())
