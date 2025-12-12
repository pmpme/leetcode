# Q3. Largest Rectangle in Histogram
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        res = 0
        stack = [] # (left_idx, height)

        for r, curr in enumerate(heights): # right end, height that won't be included
            start = r   # index to consider in future iteration
            
            # ONLY if considering THIS round and not deferring to future consideration
            while stack and stack[-1][1] > curr: # if prev/left height is larger
                l, prev = stack.pop() # then we don't want to miss out on gains
                res = max(res, (r - l) * prev) # so check if area beats prev area
                start = l # utilize, max out the left side
            
            stack.append((start, curr)) # add index and value for future consideration

        while stack: # remaining heights to the left
            l, height = stack.pop()
            res = max(res, (N - l) * height) # check against the end
            # remember, given above logic, no remaining height will be larger than end

        return res

"""
draw out the heights
"""