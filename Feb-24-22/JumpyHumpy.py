# Problem Link : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/jumpy-humpy-5e0231d6/

import copy
arrayLength = int(input())
heights = list(map(int, input().split()))

stamina = copy.deepcopy(heights)
stack = []
for i in range(arrayLength-1, -1, -1):
    while len(stack) > 0 and heights[stack[-1]] < heights[i]:
        stack.pop()
    if len(stack) > 0:
        stamina[i] = stamina[i] ^ stamina[stack[-1]]
    stack.append(i)

print(max(stamina))
