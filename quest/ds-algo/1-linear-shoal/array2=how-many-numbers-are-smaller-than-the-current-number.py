# Q2. How Many Numbers Are Smaller Than the Current Number
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        vals = sorted(nums)
        cur = vals[0]
        counts = { cur: 0 }
        cnt = 1
        res = [1] * len(nums)

        for i in range(1, len(vals)): # starting with 2nd num
            val = vals[i] 
            if val != cur:          # if it is new num
                counts[val] = cnt   # then add count smaller than it
                cur = val           # and update as the new cur num
            cnt += 1    # continue count either way

        for i, num in enumerate(nums):
            count_smaller = counts[num]
            res[i] = count_smaller
        
        return res


"""
given list of nums
where values are not unique
nor sorted

return list of counts, where each count is 
    the count of nums less than the num 
    in corresponding index position
           
                1 2 2 1 1  # counts
[8,1,2,2,3] => [1,2,2,3,8]
[4,0,1,1,3] 
            => [(1,1), (2,2), (3,1), (8,1)] # counts: {num: count}
            => [(1,0), (2,1), (3,3), (8,4)] # smaller: {num, accumulatedCount}

[6,5,4,8]
[2,1,0,3]

[7,7,7,7]
[0,0,0,0]
"""