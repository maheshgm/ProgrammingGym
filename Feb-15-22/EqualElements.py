# Problem Link : https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/equal-elements-2-db70c1ae/

testCases = int(input())

for test in range(testCases):
	noOfElements = int(input())
	arrayA = list(map(int,input().split()))

	evenCount,oddCount = 0,0
	for index in range(noOfElements):
		element = arrayA[index]
		if element & 1 == 0:
			evenCount+=1
		else:
			oddCount+=1

	print(min(evenCount,oddCount))


