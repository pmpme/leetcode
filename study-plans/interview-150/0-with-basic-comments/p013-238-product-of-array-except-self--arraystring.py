#!/usr/bin/python3
# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
from typing import List
import pdb

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

Strategy:
    Track a prefix going from Left -> Right
        representing the product so far, excluding the current number
    So from left to right, start prefix at 1
        then with each new number
            first take on the incoming prefix (since we want the product excluding self)
            then after multiply current number to the prefix for future consideration
        at the end we have result of left-products at each position excluding self
    Next, from right to left, start suffix at 1
        then with each new number
            first take on incoming suffix, and multiply it into current res value 
                (which contains just the product of all nums to the left of curr num)
            then after multiply current number to suffix for future consideration
        at the end we merged the right products as well

Input: nums = [1,2,3,4]  -->  Output: [24,12,8,6]

LEFT -> RIGHT
-------------
            [1, 2, 3, 4]
result       1  1  2  6     <== take this
prefix   1,  1  2  6  24


RIGHT -> LEFT
--------------
result      [1, 1, 2, 6]
suffix                    1
new result   24 12 8  6
original      1  2 3  4
new suffix   24 24 12 4

"""