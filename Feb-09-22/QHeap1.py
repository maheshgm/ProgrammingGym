# Problem Link : https://www.hackerrank.com/challenges/qheap1/problem

import heapq

noOfQueries = int(input())

deletedElements = {}
minHeap = []

heapq.heapify(minHeap)


for query in range(noOfQueries):
    queryItem = list(map(int,input().split()))

    if queryItem[0] == 1:
        heapq.heappush(minHeap, queryItem[1])
    elif queryItem[0] == 2:
    	if queryItem[1] in deletedElements:
    		deletedELements[queryItem[1]] += 1
    	else:
    		deletedElements[queryItem[1]] = 1
    else:
    	minElement = 10**9
    	while True:
    		minElement = minHeap[0]
    		if minElement in deletedElements:
    			heapq.heappop(minHeap)
    			deletedElements[minElement] -= 1
    			if deletedElements[minElement] <= 0:
    				del deletedElements[minElement]
    		else:
    			break
    	print(minElement)

