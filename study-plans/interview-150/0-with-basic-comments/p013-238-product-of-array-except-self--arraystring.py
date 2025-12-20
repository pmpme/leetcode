#!/usr/bin/python3
# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


"""
Given a list of nums
    return a list of vals representing at each position
        then product of all other numbers except itself

Strategy:
    Go left to right and get products
    Go right to left and get products
    Go once more and multiply left by right, excluding current
    Return calculated values

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""