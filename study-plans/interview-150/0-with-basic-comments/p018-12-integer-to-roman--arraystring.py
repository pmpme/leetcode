#!/usr/bin/python3
# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/
from typing import List
import pdb

class Solution:
    def intToRoman(self, num: int) -> str:
        codes = []

        for val, code in self.get_vals():
            while num >= val:
                codes.append(code)
                num -= val

        return ''.join(codes)
        
        
    def get_vals(self):
        return [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]