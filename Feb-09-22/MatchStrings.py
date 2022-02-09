# Problem Link : https://www.hackerrank.com/challenges/sparse-arrays/problem

from collections import Counter

# Read the input for strings
noOfStrings = int(input())
strings = []
for string in range(noOfStrings):
	strings.append(input())

# compute the frequency of the strings read above
frequency = Counter(strings)

noOfQueries = int(input())

# for every query print the result which is the count of each query word
for query in range(noOfQueries):
	queryString = input()
	if queryString not in strings:
		print(0)
	else:
		print(frequency[queryString])

