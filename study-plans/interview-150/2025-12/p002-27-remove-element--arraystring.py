#!/usr/bin/python3
# 27. Remove Element
# https://leetcode.com/problems/remove-element/
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        nxt = 0

        for i in range(N):
            if nums[i] != val:
                nums[nxt] = nums[i]
                nxt += 1
        
        return nxt

"""
Given a list of numbers and a value
remove all occurrences of value from numbers, in-place
and return the total numbers which are not value
aka the length of the new list part after removing value
order does not matter

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]

Logic:
Keep track of next insert position
Then iterate each num and if it is not equal to value to be removed
    then add to next insert position
    and increment insert position
Return whatever next insert position points to
    which will match the total number of non-value nums
"""