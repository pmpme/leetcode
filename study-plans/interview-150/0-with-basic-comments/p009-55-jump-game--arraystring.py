#!/usr/bin/python3
# 55. Jump Game
# https://leetcode.com/problems/jump-game/
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        reach = 0

        for i in range(N):
            if reach < i:
                return False
            
            reach = max(reach, i + nums[i])
            if reach >= (N - 1):
                break

        return True

"""
Given some nums, 
    where value at each index position,
    is the jumpable amount
And the goal is to reach the end of nums

Strategy:
Track the reachable point - starting at 0 / first position
Now iterate each num, whilte possible (while reach-able)
    if every we reach a position that is < reach, return False
Otherwise, get the jump amount and update reach if futher index unlocked
And if that unlocked index is the last one, we succeeded, and return True
"""