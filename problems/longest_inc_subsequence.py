"""
A subsequence is not the same as a subarray.
A subarray is contiguous (e.g., [2,5,3]).
A subsequence is derived by deleting some elements without changing
the order of the remaining elements.
For [10,9,2,5,3,7,101,18], [2,3,7,101] is a subsequence (we skipped 5). We cannot reorder numbers.


Example 1: nums = [10,9,2,5,3,7,101,18] → Output: 4 ([2,3,7,101] or [2,5,7,101] or [2,3,7,18]).
Example 2: nums = [0,1,0,3,2,3] → Output: 4 ([0,1,2,3]).
Example 3: nums = [7,7,7,7,7] → Output: 1 (strictly increasing, so duplicates don't count).

Imagine you are reading the array from left to right. For every element nums[i], ask yourself:
"
If I decide that nums[i] is the last element of my increasing subsequence,
what is the longest subsequence I can build ending here?
"
To answer that, you must look back at all previous elements nums[j]
where j < i. If nums[j] < nums[i],
then you can take the best subsequence ending at j and simply append nums[i] to it.
"""

import bisect


def length_of_lis(arr):
    """
    Time: O(n²), Space: O(n). This works for n ≤ 2500.
    """
    n = len(arr)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp) if dp else 0


def longest_increase_subsequence(arr):
    """
    Patience Sorting (O(n log n))	O(n log n)	O(n)
    """
    tail = []
    for num in arr:
        pos = bisect.bisect_left(tail, num)
        if pos == len(tail):
            tail.append(num)
        else:
            tail[pos] = num
    return len(tail)


"""
[10,9,2,5,3,7,101,18]

x=10: tails = [10]
x=9: bisect_left([10], 9) = 0 → replace → tails = [9]
x=2: bisect_left([9], 2) = 0 → replace → tails = [2]
x=5: bisect_left([2], 5) = 1 → append → tails = [2,5]
x=3: bisect_left([2,5], 3) = 1 → replace → tails = [2,3]
(Note: We replaced 5 with 3. We lost the subsequence [2,5] but gained [2,3]
which is better for future numbers like 4, 7, etc.)
x=7: bisect_left([2,3], 7) = 2 → append → tails = [2,3,7]
x=101: bisect_left([2,3,7], 101) = 3 → append → tails = [2,3,7,101]
x=18: bisect_left([2,3,7,101], 18) = 3 → replace → tails = [2,3,7,18]
"""


if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    res_1 = length_of_lis(arr)
    res_2 = longest_increase_subsequence(arr)

    print(res_1, res_2)
