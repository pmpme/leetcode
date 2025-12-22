#!/usr/bin/python3
# 134. Gas Station
# https://leetcode.com/problems/gas-station/
from typing import List
import pdb

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        N = len(gas)
        tank = 0
        start = 0

        for i in range(N):
            tank += gas[i]
            tank -= cost[i]

            if tank < 0:
                tank = 0
                start = i + 1
            
        return start

"""
Given a 2 lists of nums,
    1 list is gas to add to tank on arrival
    1 list is cost to remove from tank on departure
Goal is to find if we can make a full loop, and if so
    from what gas station should we start to make full loop.

The key is that there IS* a solution, and a unique one,
    as long as the total gas is > total cost
The subsequent key is that we only need the start, meaning
    when we reset the tank because the tank falls below 0,
    this works because we don't care that maybe there is 
    lots of tank that gets carried over from previous spots.
    Because we are seeking when we start** this rules out
    current spot, because should we start from current,
    we would not have enough gas to continue.
"""
