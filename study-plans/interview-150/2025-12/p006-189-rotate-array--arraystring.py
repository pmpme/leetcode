#!/usr/bin/python3
# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/
from typing import List

class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        N = len(nums)
        k %= N
        reverse(0, N - 1)
        reverse(0, k - 1)
        reverse(k, N - 1)

    def rotate_tle(self, nums: List[int], k: int) -> None:
        N = len(nums)
        k %= N
        for _ in range(k):
            last = nums[N - 1]
            for i in range(N - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = last

"""
Given a list of nums, and a position k
    rotate nums so that 
        the last k nums appear as the first k nums, and
        the nums preceding k nums are shifted to the right by k slots

Strategy:
    The "trick" is to reverse nums,
        then take first k nums and reverse back
        then reverse the remaining nums
    [1,2,3,4,5,6,7], k=3
    [7,6,5,4,3,2,1], reverse
    [5,6,7,4,3,2,1], reverse back first k (originally last k)
    [5,6,7,1,2,3,4], reverse back remaining (originally before last k)

    The manual way is to do below for k iterations
        take/hold/remember last number
        then shift the rest 1 forward
        then set first num as taken/held/remembered num
    This works because we remember the last num
        then work backwards and fill curr pos with prev num
        then when 2nd pos is filled with 1st num
            then 1st pos can be filled with prev last num
            (simulating a rotation by 1 position) 
"""