# Q2. Shuffle the Array
from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res

"""
nums with even length
as if, divide evenly in half
return left and right half values, in order

               a b c a b c
Input: nums = [2,5,1,3,4,7], n = 3
         a a b b c c
Output: [2,3,5,4,1,7] 
"""