# Problem Link: https://www.codechef.com/ICPCTR05/problems/MAXDIVER

from collections import Counter

testCases = int(input())
for test in range(testCases):
	noOfElements , maxOps = map(int,input().split())
	elements = list(map(int,input().split()))

	frequency = Counter(elements)

	maxDiversity = noOfElements * (noOfElements-1) // 2

	for ele in frequency:
		maxDiversity -= frequency[ele] * (frequency[ele] - 1) // 2

	duplicates = list(filter(lambda ele: ele > 1, frequency.values()))
	duplicates.sort()

	while len(duplicates)>0 and maxOps>0:
		
		ele = duplicates[-1]
		
		del duplicates[-1]
		if ele > 1:
			maxOps -= 1
			ele -= 1
			maxDiversity += ele
		if(ele > 1):
			duplicates.append(ele)
			duplicates.sort()
	print(maxDiversity)
