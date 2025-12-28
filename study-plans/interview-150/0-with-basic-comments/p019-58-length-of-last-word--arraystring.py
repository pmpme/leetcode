#!/usr/bin/python3
# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/
from typing import List
import pdb

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.split()[-1])

        chars = [c for c in s]
        count = 0

        while chars and chars[-1] == ' ':
            chars.pop()

        while chars and chars[-1] != ' ':
            chars.pop()
            count += 1

        return count