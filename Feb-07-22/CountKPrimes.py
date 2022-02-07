# Problem Link 		: https://www.codechef.com/LRNDSA05/problems/KPRIME/
# Difficulty level 	: Medium-Hard
# Topic 			: Maths

from math import *
MAX_LIMIT = 10**5 + 3
seiveTable = [ 0 for i in range(MAX_LIMIT)]
seiveTable[0],seiveTable[1] = -1,-1

for number in range(MAX_LIMIT):
	if seiveTable[number] == 0:
		seiveTable[number] = 1
		for factor in range(number*2, MAX_LIMIT, number):
			seiveTable[factor] += 1

kPrimeCount = [[0,0,0,0,0] for i in range(MAX_LIMIT)]
for number in range(MAX_LIMIT):
	kPrimeCount[number] = list(kPrimeCount[number-1])
	if 1<=seiveTable[number]<=5:
		kPrimeCount[number][seiveTable[number]-1] += 1

for _ in range(int(input())):
	A,B,K = map(int,input().split())
	print(kPrimeCount[B][K-1] - kPrimeCount[A-1][K-1])
