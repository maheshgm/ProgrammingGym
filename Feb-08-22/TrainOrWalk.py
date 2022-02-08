# Problem Link: https://www.codechef.com/ICPCTR05/problems/WALKFAST

testCases 	= int(input())
for test in range(testCases):
	noOfCities,cityA,cityB,cityC,cityD,walkingSpeed,trainSpeed,depTime 	= map(int,input().split())
    
	locations = list(map(int,input().split()))
    
	onlyWalkTime = abs(locations[cityB-1] - locations[cityA-1])*walkingSpeed

	onTakingTrain = 10**7 + 1

	timeTakenToTakeTrain = abs(locations[cityC-1] - locations[cityA-1])*walkingSpeed
	if timeTakenToTakeTrain <= depTime:
		onTakingTrain = depTime + abs(locations[cityD-1] - locations[cityC-1])*trainSpeed + abs(locations[cityD-1]-locations[cityB-1])*walkingSpeed

	print(min(onTakingTrain,onlyWalkTime))
