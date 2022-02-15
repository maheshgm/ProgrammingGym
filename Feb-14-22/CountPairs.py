# Problem Link : https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/count-pairs-10-9cfeeb36/

MAX_RANGE = 10**6 + 2

testCases = int(input())
for test in range(testCases):
	noOfElements = int(input())
	X = int(input())
	Y = int(input())

	arrayA = list(map(int,input().split()))
	arrayB = list(map(int,input().split()))

	arrayC = [0]*MAX_RANGE

	for element in arrayA:
		index = (element&X) ^ (element&Y)
		arrayC[index] += 1

	result = 0
	for element in arrayB:
		index = (element&X) ^ (element&Y)
		result += arrayC[index]

	print(result)