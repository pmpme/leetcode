# Q3. Max Consecutive Ones
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
                res = max(res, cur)
            else:
                cur = 0
        
        return res
