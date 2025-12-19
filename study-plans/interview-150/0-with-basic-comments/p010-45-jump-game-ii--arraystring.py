#!/usr/bin/python3
# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0               # the window, inclusive
        goal = len(nums) - 1    # last position
        jumps = 0               # count jumps, of windows

        while r < goal:         # get to the last position
            reach = r           # we can at least reach the window range end
            for cur in range(l, r + 1): # check each position in range
                # can we reach further by jumping value at cur position
                reach = max(reach, cur + nums[cur]) 
            l = r + 1   # new window start is immediately after cur window
            r = reach   # new window end is farthest we can reach
            jumps += 1  # with each window, we pay with a jump

        return jumps    # return total cost

"""
Given a list of nums
Goal is to reach the last position
We start at first position without cost
    So our start window is the 1st position
Then the next window is where we can reach
    which is cur position + jump value at cur position
Every time we exhaust our window, we add the jump

And it is guaranteed we can reach the end
    So an input like [2,0,0,0,0,0] is invalid

"""
