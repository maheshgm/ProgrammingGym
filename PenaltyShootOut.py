# Problem Link : https://www.codechef.com/LRNDSA02/status/PSHOT

testCases = int(input())
for test in range(testCases):
	noOfShots = int(input())
	win_lose = input()

	lengthOfString = 2*noOfShots
	left_a, left_b, curr_a, curr_b, flag = noOfShots,noOfShots,0,0,lengthOfString
	for shot in range(lengthOfString):
		if win_lose[shot] == '1':
			if shot & 1 == 0:
				curr_a += 1
			else:
				curr_b += 1
		if shot & 1 == 0:
			left_a -= 1
		else:
			left_b -= 1
		if curr_a > curr_b + left_b:
			flag = shot + 1
			break
		if curr_b > curr_a + left_a:
			flag = shot + 1
			break
	print(flag)