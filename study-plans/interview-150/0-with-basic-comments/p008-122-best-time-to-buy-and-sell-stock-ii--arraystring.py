#!/usr/bin/python3
# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day, last_day = 0, len(prices) - 1
        profits = 0

        while day < last_day:
            # find smaller price
            while day < last_day and prices[day + 1] <= prices[day]:
                day += 1
            buy = prices[day]
            # find higher price
            while day < last_day and prices[day + 1] >= prices[day]:
                day += 1
            sell = prices[day]
            # add to profits
            profits += (sell - buy)

        return profits

"""
Given a list of prices of stocks for each day,
    where we can sell and by on the same day,
    just as long as we're not holding more than 1 stock at a time,
Goal is to find and return the maximum profit

Strategy:
    Try below until all days exhausted
    First seek next day with lower price -> and buy
        Then seen next day with higher price -> and sell
        Then add this to profits -> and continue
        Note that at this point the day still points to the sell day
            So as long as the next day price is higher, we'll
                still explore current day for continued transactions
                because lower price allows bigger profits
"""
