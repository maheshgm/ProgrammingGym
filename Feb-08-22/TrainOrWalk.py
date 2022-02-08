# Problem Link: https://www.codechef.com/ICPCTR05/problems/WALKFAST

testCases 	= int(input())
for test in testCases:
	noOfCities,cityA,cityB,cityC,cityD,walkingSpeed,trainSpeed,depTime 	= map(int,input().split())

	locations = list(map(int,input().split()))

	onlyWalkTime = abs(locations[cityB] - locations[cityA])*walkingSpeed

	onTakingTrain = onlyWalkTime

	timeTakenToTakeTrain = abs(locations[cityC] - locations[cityA])*walkingSpeed
	if timeTakenToTakeTrain <= depTime:
		onTakingTrain = depTime + abs(locations[cityD] - locations[cityC])*trainSpeed + abs(locations[cityD]-locations[cityB])

	print(min(onTakingTrain,onlyWalkTime))
