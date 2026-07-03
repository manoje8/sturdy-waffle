from sortedcontainers import SortedList


def medianSlidingWindow(nums, k):
    median = SortedList(nums[:k])
    result = []

    def get_median():
        if k % 2 == 1:
            return float(median[k // 2])
        return (median[k // 2 - 1] + median[k // 2]) / 2

    result.append(get_median())

    for i in range(k, len(nums)):
        median.remove(nums[i - k])
        median.add(nums[i])
        result.append(get_median())

    return result


def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    arr = nums1 + nums2
    arr.sort()
    n = len(arr)

    def find_median():
        if n % 2 == 1:
            return float(arr[n // 2])
        return (arr[n // 2 - 1] + arr[n // 2]) / 2

    return find_median()


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    k = 3
    res = medianSlidingWindow(nums=nums, k=4)
    print(res)
