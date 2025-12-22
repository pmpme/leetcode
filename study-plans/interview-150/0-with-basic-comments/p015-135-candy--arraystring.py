#!/usr/bin/python3
# 135. Candy
# https://leetcode.com/problems/candy/
from typing import List
import pdb

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # every child should have at least 1 candy, regardless of rating
        # child with higher rating relative to adjacent peers, should have more candy
        # find minimum required - meaning, higher rating child has +1 more candy
        N = len(ratings)
        candies = [1] * N   

        # start comparing against left peer
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
            
        # then compare against the right peer
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1) # optimize for more candies

        return sum(candies) # at the end we have the minimum to satisfy conditions

