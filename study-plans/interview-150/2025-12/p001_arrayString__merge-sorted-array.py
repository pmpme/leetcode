# 88. Merge Sorted Array
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = (m + n) - 1
        m, n = m - 1, n - 1

        while pos >= 0:
            # add nums1 num if val >- other or other ran out
            if m >= 0 and (n < 0 or nums1[m] >= nums2[n]):
                nums1[pos] = nums1[m]
                m -= 1
            else: # n and (m < 0 or nums1[m] < nums2[n])
                nums1[pos] = nums2[n]
                n -= 1
            pos -= 1
        