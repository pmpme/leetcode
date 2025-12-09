# Q3. Exclusive Time of Functions

from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n   # total times
        stack = []      # functions running
        prev = 0        # last time

        for log in logs: 
            # extract function, type, timestamp
            fn, memo, curr = log.split(":")
            fn, curr = int(fn), int(curr)

            if memo == "start": # if starting
                if stack: # if another function being overtaken
                    res[stack[-1]] += curr - prev # add its paid time before taking over
                stack.append(fn) # add current function
                prev = curr # update tp current timestamp - this is when next ending func would have started (for that iteration)

            else: # if ending
                res[stack.pop()] += (curr - prev + 1) # add full duration, including end/curr time
                prev = curr + 1 # set prev timestamp (also the start of next function) as next time since curr ends current function

        return res # return accumulated times
        

""" 
single threaded CPU, execute program containing n functions
each function has unique ID between 0, n-1
functions stored in call stack
    its ID pushed to stack when function starts
    its ID popped off stack when function ends
at the top of stack is the current function being executed
return total time for each function

n = 2           => [3,4]
["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
"""