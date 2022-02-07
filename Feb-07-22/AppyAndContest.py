# Problem Link 		: https://www.codechef.com/LRNDSA05/problems/HMAPPY2
# Difficulty Level 	: Easy-Medium
# Topic 			: Maths

import math

testCases = int(input())
N,A,B,K = map(int,input().split())
NbyA = N//A
NbyB = N//B

gcdOfAB = math.gcd(A,B)
lcmOfAB = (A*B)//gcdOfAB

problemsSolved = NbyA + NbyB - 2*(N//lcmOfAB)

if problemsSolved >= K:
	print("Win")
else:
	print("Lose")
	