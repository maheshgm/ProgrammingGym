# Problem Link : https://www.codechef.com/CRKG2022/problems/CTC_001

testCases = int(input())
for tests in range(testCases):
	Items = input()
	finalProfit = 0
	costPrices = list(map(int,input().split()))
	sellingPrices = list(map(int,input().split()))

	for item in range(len(Items)):
		itemNumber = int(Items[item])
		finalProfit += sellingPrices[itemNumber] - costPrices[itemNumber]

	print(finalProfit)