#!/usr/bin/python3
# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
from typing import List
import pdb

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # find shortest word
        base = strs[0]
        for s in strs[1:]:
            if len(s) < len(base):
                base = s

        # for every char, compare nth char in every other word until no longer matching
        common = 0
        for i, c in enumerate(base):
            matching = True
            for s in strs:
                if s[i] != base[i]:
                    matching = False
            if not matching:
                break
            common = i + 1
                    
        return base[:common]
