# Problem Link : https://www.hackerrank.com/challenges/crush/problem

arraySize , operations = map(int,input().split())

array = [0]*arraySize
for op in range(operations):
	start,end,sumToAdd = map(int,input().split())

	array[start - 1] += sumToAdd

	if end < arraySize:
		array[end] -= sumToAdd


maxValue = 0
prefixSum = 0
for element in array:
	prefixSum += element
	maxValue = max(maxValue,prefixSum)

print(maxValue)