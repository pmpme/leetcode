# Q2. Evaluate Reverse Polish Notation 
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []

        for val in tokens:
            if val not in operators:
                stack.append(int(val))
                continue

            b, a = int(stack.pop()), int(stack.pop())
            if val == "+":
                stack.append(a + b)
            elif val == "-":
                stack.append(a - b)
            elif val == "*":
                stack.append(a * b)
            elif val == "/":
                stack.append(int(a / b)) # int() truncates towards 0, vs // floor division

        return stack.pop()

"""
given list of tokens in "reverse polish notation"
operators: +, -, *, /
division always truncates to 0
no division by 0

["2","1","+","3","*"] -> 9
2 + 1 = 3
3 * 3 = 9

["4","13","5","/","+"] -> 6
4 / (13 + 5)

process each char
    if not an operator, add to stack
    if an operator, remove last 2
    apply the operator, and append result back into stack
return last remaining or final result from stack

["4","13","5","/","+"]
4
4,13
4,13,5
4,13,5 -> "/" and 13,5 -> 4,2
4,2 -> "+" and 4, 2 -> 6
return 6

["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
                                          ^
10, 6, 9, 3, "+"        --> 10, 6, 12
10, 6, 12, -11, "*"     --> 10, 6, -121
10, 6, -121, "/"        --> 10, 0 !
10, 0, "*"              --> 0
0, 17, "+"              --> 17
17, 5, "+"              --> 22

6 // -121 = -1
int(6 / 121) = 0

["18"] -> 18, return as int
"""