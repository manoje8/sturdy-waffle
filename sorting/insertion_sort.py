def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        value = arr[i]
        hole = i

        while hole > 0 and arr[hole - 1] > value:
            arr[hole] = arr[hole - 1]
            hole -= 1

        arr[hole] = value


if __name__ == "__main__":
    arr = [22, 5, 3, 6, 10, 12]
    insertion_sort(arr)
    print(arr)
