#!/usr/bin/python3
# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
from typing import List
import pdb

class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        i = total = 0
        N = len(s)

        while i < N:
            # if preceding val is smaller than subsequent val
            if i + 1 < N and vals[s[i]] < vals[s[i + 1]]:
                total += vals[s[i:i+2]]
                i += 2
            else:
                total += vals[s[i]]
                i += 1
        return total
            
"""
Given a roman numeral string, return the integer value of that string

Strategy:
There are single char and double char values. 
The pattern is, if there are 2 values and the left value is < right value,
    then the 2 should be computed as a pair,
    because the full roman numeral is listed from largest to smallest

So process each char individually UNLESS the subsequent char is < curr char
    then process as a pair.
"""