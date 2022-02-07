# Problem Link		: https://www.codechef.com/LRNDSA07/problems/FROGV
# Difficulty Level	: Medium
# Topic 			: Dynamic Programming

frogCount,distance,pairedFrogs = map(int,input().split())
xCoordinates = list(map(int,input().split()))

tempCoordinate = xCoordinates[:]
xCoordinates.sort()
dictionary = {}
start = 0

for frog in range(0,frogCount-1):
	if xCoordinates[frog+1] - xCoordinates[frog] > distance:
		for frog_ in range(start, frog+1):
			dictionary[xCoordinates[frog_]] = xCoordinates[frog]
		start = frog+1

for frog in range(start,frogCount):
	dictionary[xCoordinates[frog]] = xCoordinates[frogCount-1]

for _ in range(pairedFrogs):
	u,v = map(int,input().split())
	ux,vx = tempCoordinate[u-1],tempCoordinate[v-1]

	if (dictionary[ux] >= vx and vx>=ux) or (dictionary[vx]>=ux and ux>=vx):
		print("Yes")
	else:
		print("No")
