# https://www.codechef.com/LRNDSA02/problems/NOTALLFL

testCases = int(input())

for test in range(testCases):
	numPieces, numFlavours = map(int,input().split())

	lst = list(map(int,input().split()))
	frequency = [0 for i in range(numFlavours+1) ]

	frequency[0] = 1
	maxLength = 0

	left,length = 0,0
	for right,elem in enumerate(lst):
		frequency[elem] += 1
		length += 1
		if 0 not in frequency:
			maxLength = max(maxLength, length-1)

			while 0 not in frequency:
				frequency[lst[left]] -= 1
				length -= 1
				left += 1

	maxLength = max(maxLength,length)
	print(maxLength)