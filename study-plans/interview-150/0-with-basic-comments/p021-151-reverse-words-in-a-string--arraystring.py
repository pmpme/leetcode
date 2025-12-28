#!/usr/bin/python3
# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/
from typing import List
import pdb

class Solution:
    def reverseWords(self, s: str) -> str:
        # return " ".join(s.split()[::-1])

        words = []          # collect words from the back
        i = len(s) - 1

        while i >= 0:
            word = ''

            # first ignore trailing whitespaces
            while i >= 0 and s[i] == ' ':
                i -= 1

            # then collect chars in next word
            while i >= 0 and s[i] != ' ':
                word = s[i] + word
                i -= 1
            
            if word: # only add if not empty
                words.append(word)

        return ' '.join(words)


"""
Given a string containing chars and spaces, return string
    where the words are reversed, delimited by single space

Strategy:
A) the python way of splitting by words, reversing, then combining back
B) manual way of scanning for non empty spaces in chunks, reversing, returning
    start with chars array, then process from the back, until no chars remain
        first ignore all trailing whitespaces
        then take all chars part of same word by waiting for first whitespace
        continue loop until no chars remain
    with collected words, return, separated by a single whitespace
"""