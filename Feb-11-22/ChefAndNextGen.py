# Problem Link: https://www.codechef.com/FEB222C/problems/HELIUM3

testCases = int(input())
for test in range(testCases):
	powerPerYear, Years, HeOnMoon, powerPerUnit = map(int,input().split())

	totalPowerRequired = powerPerYear*Years

	totalPowerGenerated = HeOnMoon * powerPerUnit

	if totalPowerGenerated >= totalPowerRequired:
		print("Yes")
	else:
		print("No")
		
