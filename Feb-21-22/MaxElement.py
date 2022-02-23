#!/bin/python3
# Problem Link : https://www.hackerrank.com/challenges/maximum-element/problem?isFullScreen=true
import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
    stack = [(0,0)]
    res = []
    for op in operations:
        if op[0] == '1':
            ele = list(map(int,op.split()))[1]
            stack.append((ele, max(ele, stack[-1][1])))
        elif op[0] == '2':
            stack.pop()
        else:
            res.append(stack[-1][1])
    return res
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
