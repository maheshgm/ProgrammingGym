# Problem Link : https://www.codechef.com/LRNDSA02/problems/COMPILER

testCases = int(input())
for test in range(testCases):
	input_str = input()
	rev_str = list(input_str[::-1])

	balanced = 0
	break_balanced = 0

	for ind in range(len(input_str)):
		if input_str[ind] == '<':
			break_balanced += 1
		else:
			break_balanced -= 1

		if break_balanced == 0:
			balanced = ind + 1
		if break_balanced<0:
			break

	print(balanced)