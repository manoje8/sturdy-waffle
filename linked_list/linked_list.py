from linked_list.list import List


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        temp = List(value)

        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def insert_at(self, value, index):

        if index < 0:
            raise IndexError("Index cannot be negative")

        current = self.head

        new_node = List(value)

        if index == 0:
            new_node.next = current
            self.head = new_node
            return

        for _i in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        # if current.next is None:
        #     raise IndexError("Index out of range")

        temp = current.next

        current.next = new_node
        new_node.next = temp

    def search(self, search_value, is_recursive=False):
        node = self.head

        if is_recursive:
            return self.__recursive_search(node, search_value)
        else:
            return self.__iterative_search(node, search_value)

    def delete_at(self, index):
        temp = self.head

        if temp is None:
            raise IndexError("Cannot delete from empty list")

        if index == 0:
            self.head = temp.next
            return

        for _i in range(index - 1):
            if temp is None:
                raise IndexError("Index out of range")
            temp = temp.next

        if temp.next is None:
            raise IndexError("Index out of range")

        prev = temp
        delete_node = prev.next
        prev.next = delete_node.next

    def reverse_by_pointer(self):
        """Reverse the direction of a single linked list"""
        current = self.head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def print_out(self):
        temp = self.head
        while temp:
            print(temp.value, end=", ")
            temp = temp.next
        print("\n")

    def hasCycle(self) -> bool:
        node = self.head

        if not node or not node.next:
            return False

        slow = fast = node

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def detectCycleStart(self):
        temp = self.head

        slow = fast = temp
        has_cycle = False

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

            if slow == fast:
                has_cycle = True
                break

        if not has_cycle:
            return None

        slow = self.head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow.value

    def find_middle(self):
        temp = self.head

        if temp is None:
            return None

        slow = fast = temp

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        return slow.value

    def __iterative_search(self, node, value):
        while node:
            if node.value == value:
                return True
            node = node.next

        return False

    def __recursive_search(self, node, value):

        if node is None:
            return False

        if node.value == value:
            return True
        else:
            return self.__recursive_search(node.next, value)
