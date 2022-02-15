# Problem Link : https://www.hackerearth.com/practice/basic-programming/operators/basics-of-operators/practice-problems/algorithm/going-to-office-e2ef3feb/

distance = int(input())

online_taxi = list(map(int,input().split()))
classic_taxi = list(map(int,input().split()))

price_of_online_taxi = online_taxi[0] + (distance - online_taxi[1]) * online_taxi[2]
price_of_classic_taxi = classic_taxi[1] + (distance//classic_taxi[0]) * classic_taxi[2] + (distance) * classic_taxi[3]

if price_of_online_taxi <= price_of_classic_taxi:
	print("Online Taxi")
else:
	print("Classic Taxi")