# Problem Link : https://www.hackerearth.com/practice/basic-programming/operators/basics-of-operators/practice-problems/algorithm/let-us-understand-computer-78476e7a/

testCases = int(input())
for test in range(testCases):

	number = int(input())
	start = 1
	resultFactors = 0
	while start*start <= number:

		start *= 2
		if number//start >= start//2:
			resultFactors = number - number//start
		else:
			resultFactors = number - (start//2) + 1
			
	print(resultFactors)