#!/usr/bin/python3
# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for today in prices[1:]:
            profit = max(profit, today - buy)
            buy = min(buy, today)
            
        return profit

"""
Given a list of prices, each representing a day
    where we can buy on a day, and sell on a different+future day
    we're trying to maximize profit

Strategy
    Start buy on 1st day
    Go to next day (we can on sell on a different future day)
    If we sell today, can we beat current best profit?
    If so log
    Then also, today's price - is it lower than current buy price?
    If so update to lower price - buy low, sell high, best profit
"""
