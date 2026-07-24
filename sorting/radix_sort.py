def counting_sort(arr, m):
    n = len(arr)

    result = [0] * n

    count = [0] * 10

    for i in range(0, n):
        index = (arr[i] // m) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // m
        result[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0

    for i in range(0, len(arr)):
        arr[i] = result[i]


def radix_sort(arr):
    m = max(arr)

    exp = 1

    while m / exp >= 1:
        counting_sort(arr, exp)
        exp *= 10


if __name__ == "__main__":
    arr = [22, 5, 3, 6, 10, 12]
    radix_sort(arr)
    print(arr)
