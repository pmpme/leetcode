# Q3. Find All Numbers Disappeared in an Array
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # -- using extra space
        # expected = set(range(1, len(nums) + 1))
        # actual = set(nums)
        # return list(expected - actual)

        # -- without extra space
        for i in range(len(nums)):
            num = abs(nums[i])  # the actual number
            pos = num - 1       # the corresponding index position
            if nums[pos] > 0:   # if not already marked as seen
                nums[pos] *= -1  # mark as seen
            # print(f'i={i}, num={num} pos={pos}, nums={nums}')

        missing = []    # not considered extra space
        for i, num in enumerate(nums):
            if num > 0: # if num at position not yet marked as seen
                missing.append(i + 1)   # then its position indicates missing num

        # print(missing)
        return missing

"""
given array of nums from 1 to n, return all nums missing in array

[4,3,2,7,8,2,3,1]

extra - same O(N) time without using extra space?
since exactly 1->n is expected, and each num is positive
    iterate each num in order
        and mark its value at its index position
        where if num is 1, mark whatever num at index 0 (val - 1) as negative
    iterate round 2
        and wherever index position was not marked
            is num which is disappeared/never appeared in array
"""