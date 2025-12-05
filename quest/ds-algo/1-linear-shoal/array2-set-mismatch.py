# Q1. Set Mismatch
from typing import List
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dupe, need = None, None
        counts = Counter(nums)
        for num in range(1, len(nums) + 1):
            if num not in counts:
                need = num
            elif counts[num] == 2:
                dupe = num
            if dupe and need:
                return [dupe, need]
        return [-1, -1]

"""
nums should be values 1 to n, every value
1 is duplicated, 1 is missing
return [duplicated, missing]

[1,2,2,4] -> [2,3]
[1,1] -> [1,2]
[2,2] -> [1,2]          # dupe may precede missing
[3,3,1] -> [3,2]        # not necessarily sorted
[3,2,3,4,6,5] -> [3,1]  # not necessarily adjacent
"""