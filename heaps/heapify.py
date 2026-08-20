"""
Heapify
0's based indexing
"""


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return (2 * i) + 2


def max_heapify(arr, i, n):
    l = left(i)
    r = right(i)

    largest = l if l < n and arr[l] > arr[i] else i

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, n)


def min_heapify(arr, i, n):
    l = left(i)
    r = right(i)

    smallest = l if l < n and arr[l] < arr[i] else i

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest, n)


def build_heapify(arr: list[int]):
    n = len(arr) // 2

    for i in range(n - 1, -1, -1):
        max_heapify(arr, i, len(arr))


if __name__ == "__main__":
    arr = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    arr1 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    min_heapify(arr, 2, len(arr))
    build_heapify(arr1)

    print(arr1)
