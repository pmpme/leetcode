#!/usr/bin/python3
# 169. Majority Element
# https://leetcode.com/problems/majority-element/
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        prev, cnt = nums[0], 1
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr == prev:
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    prev = curr
                    cnt = 1
        return prev        


"""
Given a list of nums, there is 1 num which appears more than half the time,
    there is 1 num which is the majority element
Find this num in linear time and with O(1) space

Strategy:
    Since the majority num will appear more than 1/2 the time, we use this.
    Keep track of last number and its count
        if cur number == last number, then increment count
        elif cur number != last number, then decrement count
            if decremented count is (0 or -1) takeover as new "last number"
    Is it 0 or -1? Try out to test out.
"""