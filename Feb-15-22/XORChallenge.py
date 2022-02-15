# Problem Link: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/xor-challenge-2420f189/

number = int(input())
findNumberOfBits = lambda num : len(bin(num)[2:])-1

bits = findNumberOfBits(number)

biggestNumber = (1<<bits) - 1

oneNumber = number ^ biggestNumber

maxProduct = oneNumber * biggestNumber

print(maxProduct)