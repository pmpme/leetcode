# Q2. Daily Temperatures
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for day, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = day - prev_day
            stack.append(day)

        return res 
        

"""
Goal: get number of days to wait for warmer temperature
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

 0  1  2   3  4  5  6  7
[73,74,75,71,69,72,76,73]

stack [(0, 73), ]

while stack and current temp > last stack temp
    add numdays between current day and last stack temp day
    also remove that stack item
then add current day to find future day with warmer temp
return list of days to warmer temps
"""