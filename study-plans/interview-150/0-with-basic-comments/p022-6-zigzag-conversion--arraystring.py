#!/usr/bin/python3
# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/
from typing import List
import pdb

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:                # only 1 row, means each char in its own column
            return s
        if  numRows >= len(s):          # rows count exceeds string length, so all in one column
            return s

        rows = [""] * numRows
        direction = 1                   # 1 for down, -1 for up
        row = 0                         # start on 1st row

        for c in s:
            rows[row] += c              # add char to row
            
            if row == 0:                # if on first row, continue to move down
                direction = 1
            elif row == numRows - 1:    # if on last row, continue to move up
                direction = -1

            row += direction            # determine next row, down or up

        return "".join(rows)            # return string row by row

"""
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
P   A   H   N
A P L S I I G
Y   I   R

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Input: s = "A", numRows = 1
Output: "A"
"""