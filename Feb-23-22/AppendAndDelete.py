#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here

    i = 0
    while i < len(s) and i < len(t) and s[i] == t[i]:
        i += 1
    noOfDeleteOps = len(s) - i
    noOfInsertOps = len(t) - i
    if i == len(s) and i != len(t):
        return "No"
    if noOfInsertOps + noOfDeleteOps <= k:
        return "Yes"
    else:
        return "No"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
