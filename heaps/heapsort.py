from heaps.heapify import build_heapify, max_heapify

"""
The heapsort algorithm
The heapsort algorithm starts by using BUILD-MAX-HEAP to build a max-heap on the input array

The HEAPSORT procedure takes time O.n lg n, since the call to BUILD-MAXHEAP takes time O.n
and each of the n 1 calls to MAX-HEAPIFY takes time O.lg n.
"""


def heap_sort(arr):

    build_heapify(arr)

    n = len(arr) - 1

    for i in range(n, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)
