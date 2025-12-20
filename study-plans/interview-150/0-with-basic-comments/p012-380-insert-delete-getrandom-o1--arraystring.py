#!/usr/bin/python3
# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/
from typing import List
import random

class RandomizedSet:

    def __init__(self):
        self.vals = set()

    def insert(self, val: int) -> bool:
        # Add value if not present
        # Return whether or not adding occurred
        if val in self.vals:
            return False
        self.vals.add(val)
        return True

    def remove(self, val: int) -> bool:
        # Remove value if present
        # Return whether or not removing occurred
        if val not in self.vals:
            return False
        self.vals.remove(val)
        return True

    def getRandom(self) -> int:
        # Return random value from set
        # Guaranteed to be called only when values present
        return random.choice(tuple(self.vals))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()