import math

from heaps.heapify import build_heapify, max_heapify, parent


def heap_maximum(arr):
    return arr[0]


"""
Move from top to bottom
"""


def heap_extract_max(arr):
    build_heapify(arr)
    n = len(arr) - 1
    if n < 1:
        return "Heap underflow"

    max = arr[0]

    arr[0] = arr[n]
    del arr[n]

    max_heapify(arr, 0, n - 1)

    return max


"""
Move from bottom to top
"""


def heap_increase_key(arr, i, key):
    if key < arr[i]:
        print("New key is smaller than current Key")
        return
    arr[i] = key

    print(arr[parent(i)], arr[i], i)

    while i > 0 and arr[parent(i)] < arr[i]:
        arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
        i = parent(i)


def max_heap_insert(arr, key):
    arr.append(-math.inf)
    heap_increase_key(arr, len(arr) - 1, key)


arr = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]

max_heap_insert(arr, 10)

print(arr)
