#!/usr/bin/python3
# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
from typing import List
import pdb

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = min(strs, key=len)
        
        for i, c in enumerate(base):
            for s in strs:
                if s[i] != base[i]:
                    return base[:i]

        return base

"""
Given a list of strings,
    return the longest common prefix

Strategy:
    Start with the shortest word, because at best we'll return this
    Then go through each nth char in word
        and compare to every other word's nth char
        and if matching, then continue
            else return chars up to but not including current non-matching char

Input: strs = ["flower","flow","flight"]
Output: "fl"

Here, take "flow" as the base word
    then take each char, starting from "f" then "l" then "o" etc
        and compare with same nth char in every other word
        if matching, continue... we continue until we hit "i" in "flight"
            so return all chars up to but not including "i" at index 2
"""