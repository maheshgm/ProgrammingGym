# Problem Link : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/confusion-1/

noOfElements , noOfQueries = map(int,input().split())

arrayA = list(map(int,input().split()))
unique_elements = set()
answers = [0 for i in range(noOfElements+1)]

for i in range(noOfElements-1,-1,-1):
	if arrayA[i] not in unique_elements:
		answers[i] += 1
		unique_elements.add(arrayA[i])

	answers[i] = answers[i] + answers[i+1]

for q in range(noOfQueries):
	query = int(input())
	print(answers[query-1])