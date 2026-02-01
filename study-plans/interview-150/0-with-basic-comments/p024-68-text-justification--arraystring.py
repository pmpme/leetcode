#!/usr/bin/python3
# 68. Text Justification
# https://leetcode.com/problems/text-justification/
from typing import List
import pdb

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        row = []      # active row being built
        letters = 0   # total letters in current build words

        for word in words:
            min_spaces = len(row) # spaces only between* N words is N - 1
            if letters + len(word) + min_spaces > maxWidth:
                # ** if single word in non-last row, then add spaces to that single word
                cnt = max(1, len(row) - 1) # words to add spaces to (all excluding last)
                total_spaces = maxWidth - letters # total spaces to fill between words
                for i in range(total_spaces): # use up all spaces
                    idx = i % cnt # round robin get next nth idx
                    row[idx] += ' ' # and add space to it, round robin style
                row_str = ''.join(row) # create single row string from parts
                res.append(row_str)     # add row to result
                row, letters = [], 0    # and reset row trackers

            # process next word, regardless of whether or not above executed
            row.append(word)        # add next word to row to be processed
            letters += len(word)    # account for its size, total chars

        last_row = ' '.join(row)    # whatever remains after all words processed is the last row
        last_spaces = ' ' * (maxWidth - len(last_row)) # add it plus spaces required to fill width
        res.append(last_row + last_spaces)  
        return res
