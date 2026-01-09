#!/usr/bin/python3
# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
from typing import List
import pdb

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #return haystack.index(needle) if needle in haystack else -1

        h, n = len(haystack), len(needle)

        for i in range(n - 1, h):
            curr = haystack[i - (n - 1): i + 1]
            if curr == needle:
                return i - (n - 1)
        
        return -1

"""
Given 2 strings, a <haystack> and a <needle>
    Return index of first <needle> else -1

Check haystack from left to right, in the size of the needle
    Start from the end of the first needle-length
    Check substring the size of needle, ending at current char
    If this matches our needle, return the index of needle's first char
    Else continue search
Return -1 if not found

---------------------------------------------
Input: haystack = "sadbutsad", needle = "sad"
                   012345678             012
                   size = 9              = 3
Output: 0

012345678
sadbutsad
  ^
"""