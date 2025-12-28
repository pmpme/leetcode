#!/usr/bin/python3
# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/
from typing import List
import pdb

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        codes = []

        for cur, code in values:
            count = num // cur
            codes.append(code * count)
            num -= cur * count
        
        return ''.join(codes)
        
"""
Given an integer number
    return the roman numeral equivalent

The symbols go up to 1000 - "M"
values = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

Examples: 
    3749    -> MMMDCCXLIX
    58      -> LVIII
    1994    -> MCMXCIV

Strategy:
    Go from larger roman numeral values and continuously remove
        from the starting number until all roman numerals are used
    So, because 10 (X) comes before (IX), which comes before (V), 
        which comes before (IV), which comes before (I),
        something like 34 will 
            use up X 3 times
            will pass on IX and V
            then use up IV
            then no number will remain to require I
        to return XXXIV
"""