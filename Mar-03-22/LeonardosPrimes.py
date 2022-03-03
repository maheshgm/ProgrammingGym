# Problem Link : https://www.hackerrank.com/challenges/leonardo-and-prime/problem

import math
import os
import random
import re
import sys

def primeCount(n):
    # Write your code here
    primesList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    count = 0
    product = 1
    for prime in primesList:
        product *= prime
        if product <= n:
            count += 1
    return count

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        print(str(result))


