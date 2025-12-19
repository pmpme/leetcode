#!/usr/bin/python3
# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        nxt = 2

        for i in range(2, N):
            if nums[i] == nums[nxt - 1] == nums[nxt - 2]:
                continue
            nums[nxt] = nums[i]
            nxt += 1
        
        return nxt

"""
Given list of nums already sorted in non-descending order,
    remove any number which is repeated more than 2x

Strategy:
    First, we start with 3rd number, 
        because the 2nd num will be valid whether it repeats prior or not
    Then with every subsequent number, 
        insert at next insert position ONLY IF
        the number is not repeating the previous 2 numbers

Time: Linear O(N)
Space: Constant O(1), variables only
"""