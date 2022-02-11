# Problem Link: https://www.codechef.com/FEB222C/problems/WCC

testCases = int(input())

for test in range(testCases):
	X = int(input())
	chessRecord = input()

	
	carlson,cheff = 0,0
	for result in chessRecord:
		if result == 'C':
			carlson += 2
		elif result == 'N':
			cheff += 2
		else:
			carlson += 1
			cheff += 1
	winnerAmt = 0
	if carlson > cheff:
		winnerAmt = 60*X
	elif cheff > carlson:
		winnerAmt = 40*X
	else:
		winnerAmt = 55*X

	print(winnerAmt)