#!/usr/bin/python3
# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N, nxt = len(nums), 1

        for i in range(1, N):
            if nums[i] == nums[nxt - 1]:
                continue
            nums[nxt] = nums[i]
            nxt += 1

        return nxt

    
"""
Given array of numbers sorted non-decreasing, containing duplicates
Remove duplicates in-place, maintaining relative order
And return the total count of remaining, non-duplicate nums

Strategy:
Use the fact that nums are already sorted
Then start from 2nd number in list
And only add to next position if it doesn't repeat the previous number
    (previous to the next-position-number)
"""