# Q1. Concatenation of Array

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

"""
nums of length n
ans length 2n
ans[i] === nums[i]
ans[i + n] == nums[i]

combine array <nums> with itself?
repeat itself:
[1,2,1] -> [1,2,1,1,2,1]
[1,3,2,1] -> [1,3,2,1,1,3,2,1]
"""