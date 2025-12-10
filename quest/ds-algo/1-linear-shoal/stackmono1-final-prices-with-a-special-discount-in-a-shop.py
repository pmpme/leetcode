# Q1. Final Prices With a Special Discount in a Shop
from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        
        for i, discount in enumerate(prices):
            while stack and discount <= prices[stack[-1]]:
                prices[stack.pop()] -= discount
            stack.append(i)
        return prices