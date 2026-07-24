def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if target == arr[mid]:
            return True

        if target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False


if __name__ == "__main__":
    arr = [3, 5, 6, 10, 12, 22]
    res = binary_search(arr, 1)
    print(res)
