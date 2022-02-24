#!/bin/python3
# problem link : https://www.hackerrank.com/challenges/permutation-equation/problem
import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    revP = {}
    for i in range(len(p)):
        revP[p[i]] = i+1
    res = []
    for i in range(1,len(p)+1):
        yValue = revP[revP[i]]
        res.append(yValue)
    return res


if __name__ == '__main__':

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print('\n'.join(map(str, result)))

