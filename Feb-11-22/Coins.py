# Problem Link : https://www.codechef.com/problems/COINS

dp_table = {}
def memo_dp(amount):
	if amount in dp_table:
		return dp_table[amount]

	if amount == 0:
		return 0

	coins = amount//2, amount//3, amount//4

	maxCoins = 0
	for coin in coins:
		maxCoins += memo_dp(coin)

	dp_table[amount] = max(maxCoins, amount)
	return dp_table[amount]

while True:
	try:
		amount = int(input())
		result = memo_dp(amount)

		print(result)
		
	except Exception as e:
		break