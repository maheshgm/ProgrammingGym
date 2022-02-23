#!/bin/python3
# Problem Link : https://www.hackerrank.com/challenges/balanced-brackets/problem?isFullScreen=true
import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack = []
    for bracket in s:
        
        if bracket in "[{(":
            stack.append(bracket)
        else:
            if len(stack) == 0:
                stack.append(bracket)
                continue
            elif bracket == '}' and stack[-1] == '{':
                stack.pop()
            elif bracket == ']' and stack[-1] == '[':
                stack.pop()
            elif bracket == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(bracket)
    return "YES" if len(stack)==0 else "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
