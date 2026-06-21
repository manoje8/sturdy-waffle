def merge(arr, left, right, l, r):
    i = j = k = 0

    while i < l and j < r:
        if left[i] < right[j]:
            arr[k] = left[i]
            k = k + 1
            i = i + 1
        else:
            arr[k] = right[j]
            k = k + 1
            j = j + 1

    while i < l:
        arr[k] = left[i]
        k = k + 1
        i = i + 1
    while j < r:
        arr[k] = right[j]
        k = k + 1
        j = j + 1


def merge_sort(arr, n):
    mid = n // 2

    if n < 2:
        return

    left = []
    right = []

    for i in range(mid):
        left.append(arr[i])

    for i in range(mid, n):
        right.append(arr[i])

    merge_sort(left, mid)
    merge_sort(right, n - mid)
    merge(arr, left, right, mid, n - mid)


if __name__ == "__main__":
    arr = [8, 2, 7, 6, 2, 8]
    merge_sort(arr, len(arr))
    print(arr)
