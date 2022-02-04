# Problem Link	:	"https://www.hackerrank.com/challenges/utopian-tree/problem"
# Difficulty 	: 	Moderate

def heightOfTheTree(cycleNumber):
	if cycleNumber == 0:
		return 1
	elif cycleNumber&1 == 1:
		return 2 * heightOfTheTree(cycleNumber-1)
	else:
		return 1 + heightOfTheTree(cycleNumber-1)

if __name__ == '__main__':
	tests = int(input())
	
	for _ in range(tests):
		noOfCycles = int(input())

		height = heightOfTheTree(noOfCycles)
		print(height)
		

