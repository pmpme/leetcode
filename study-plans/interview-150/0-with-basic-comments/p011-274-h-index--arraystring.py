#!/usr/bin/python3
# 274. H-Index
# https://leetcode.com/problems/h-index/
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        for i in range(len(citations) - 1, -1, -1):
            target_count = i + 1
            if citations[i] >= target_count:
                return target_count

        return 0

"""
Given a list of nums, representing count of citations per paper
Goal is to find max number of papers that was citated
    for at least that number amount

So, if citations = [1,3,1]
    There are 1 papers which were citated at least 1 times
    BECAUSE
    actual citations        [1,1,3]
    expected                [1,2,3] ****
        meaning, 
            are there 3 papers citated at least 3 times? -> NO
            are there 2 papers citated at least 2 times? -> NO
            is there 1 paper citated at least 1 time? -> YES

Strategy:
Sort citations in reverse order by value
Then iterate backwards
    In order to utilize the index positions
        where given indexes are 0-indexed
        at each index, we expect that (index + 1) number of citations

So, if citations are [3,0,6,1,5]
    There are 3 papers which were citated at least 3 times
    BECAUSE
    indexes                    [0,1,2,3,4]
    actual citations, reversed [6,5,3,1,0]
    target counts (index + 1)  [1,2,3,4,5]
    meaning
        are there 5 papers citated at least 5 times? -> NO
        are there 4 papers citated at least 4 times? -> NO
        are there 3 papers citated at least 3 times? -> YES **
        are there 2 papers citated at least 2 times? -> YES
        is there 1 paper citated at least 1 time? -> YES
    and we optimize for higher count -> show professor in best light
"""
