#!/usr/bin/python3
# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
from typing import List
import pdb

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left, right = height[0], height[-1]
        trapped = 0

        while l < r: # close in from both ends
            # move inwards on shorter wall
            if height[l] <= height[r]:
                l += 1  # make the move
                left = max(left, height[l]) # take taller of shorter 2 walls
                trapped += (left - height[l])   # add the trapped cells
            else:
                r -= 1
                right = max(right, height[r])
                trapped += (right - height[r])

        return trapped # return total trapped cells count


"""
Given a list of nums representing heights of elevations
    find total cells where water can be trapped after rain

Strategy
    Close in from left and right ends
    Moving inwards, whichever wall is shorter
        **we do this in order to implicitly handle other wall
            as in, because we move on the shorter wall
                when we compare shorter wall to another shorter wall
                then whatever is the difference can be considered trapped
                because the other-first taller wall will be taller than both shorter walls
    Then after moving inwards on the shorter wall
        take taller of it or its preceding wall, 
            then consider the current wall in relation to the taller of the 2 walls
            such that if preceding wall was taller, than we have the diff - trapped cells
            else if current wall is taller, than when we calc diff, it is 0 - no trapped cells
    Keep adding accumulating trapped values until we're all closed in
    Return total cells count
"""
