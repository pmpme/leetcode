# Q1. Build an Array With Stack Operations
from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_set = set(target) # target values
        build = [] # throwaway to track build

        ops = [] # the actual operations result to return

        for num in range(1, n + 1): # check each num
            build.append(num)   # add the num
            ops.append("Push")  # add the operation
            if num not in target_set: # if num is not in target
                build.pop()         # remove the num
                ops.append("Pop")   # add the operation
            if len(build) == len(target):   # if build has all nums
                break   # no need to continue
        
        return ops # return accrued list of operations


"""
given a LIFO stack of survived values <target>
and a <n> which means full array could have been 1->n incl
return list of "Push" or "Pop" that would have led to remaining array

Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]

For [1,2,3] to become [1,2]
we would "Push" 1   -> [1]
then "Push" 2       -> [1,2]
then "Pop" 2        -> [1]
then "Push" 3      -> [1,3]

[1,2], 4 -> ["Push","Push"] # break after built array matches target
[2,3,4], 4 -> ["Push","Pop","Push","Push","Push"]
"""