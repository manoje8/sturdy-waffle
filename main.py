from linked_list import linked_list
from linked_list.LRU import LRUCache
from linked_list.doubly_linked_list import DoubleLinkedList
from heaps.heapsort import heap_sort

def linked_fn():
    linked = linked_list.LinkedList()

    for i in [2, 4, 8, 3, 1, 5, 6, 9, 10, 7]:
        linked.insert(i)

    linked.print_out()
    linked.reverse_by_pointer()

    linked.print_out()

    print(linked.search(3))

    linked.delete_at(1)

    linked.print_out()

    print("Insert At")

    linked.insert_at(12, 9)

    linked.print_out()

    print(linked.hasCycle())

    print(linked.find_middle())


def double_linked_list():
    dl = DoubleLinkedList()
    dl.insert(2)
    dl.insert(4)
    dl.insert(6)
    dl.print_out()

def lru_fn():
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.get(3))

def sorting():
    arr = [3,2,1,5,6,4]
    heap_sort(arr)
    print(arr)

if __name__ == '__main__':
    # lru_fn()
    # linked_fn()
    # double_linked_list()
    sorting()

