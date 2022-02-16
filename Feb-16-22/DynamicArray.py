# Problem Link: https://www.hackerrank.com/challenges/dynamic-array/problem

noOfElements , noOfQueries = map(int,input().split())

arrayA = [[] for i in range(noOfElements)]
lastAnswer = 0

for query in range(noOfQueries):
	queryNo, x , y = map(int,input().split())
	if queryNo == 1:
		arrayA[(x^lastAnswer) % noOfElements].append(y)
	else:
		tempArray = arrayA[(x^lastAnswer) % noOfElements]
		lastAnswer = tempArray[ y % len(tempArray)]

		print(lastAnswer)