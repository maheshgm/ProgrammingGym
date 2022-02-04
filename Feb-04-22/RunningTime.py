# Problem Link		: "https://www.hackerrank.com/challenges/runningtime/problem?isFullScreen=true"
# Difficulty Level 	: Easy 

def InsertionSort(arrayOfNumbers, sizeOfArray):
	noOfSwaps = 0
	for i in range(1,sizeOfArray):
		firstElement = arrayOfNumbers[i]
		for j in range(i-1, -1, -1):
			if arrayOfNumbers[j] > firstElement:
				arrayOfNumbers[j+1] = arrayOfNumbers[j]
				arrayOfNumbers[j] = firstElement
				noOfSwaps += 1
			else:
				break

	return noOfSwaps

if __name__ == '__main__':
	sizeOfArray = int(input())
	arrayOfNumbers = list(map(int,input().split()))

	noOfSwaps = InsertionSort(arrayOfNumbers, sizeOfArray)
	print(noOfSwaps)