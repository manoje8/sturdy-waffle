def quick_sort(arr, start, end):
    if start < end:
        p_index = partition(arr, start, end)
        quick_sort(arr, start, p_index - 1)
        quick_sort(arr, p_index + 1, end)


def partition(arr, start, end):
    pivot = arr[end]
    p_index = start

    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index = p_index + 1

    arr[p_index], arr[end] = arr[end], arr[p_index]

    return p_index


if __name__ == "__main__":
    arr = [8, 2, 7, 6, 2, 8]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
