def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    arr = [22, 5, 3, 6, 10, 12]
    selection_sort(arr)
    print(arr)
