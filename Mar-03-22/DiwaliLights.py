# Problem Link: https://www.hackerrank.com/challenges/diwali-lights/problem

MAX_LIMIT = 100000
def exponentialPower(base, exponent):
    if exponent == 0:
        return 1
    midResult = (exponentialPower(base, exponent//2) ** 2) % MAX_LIMIT
    if exponent % 2 == 0:
        return midResult
    else:
        return (midResult * base) % MAX_LIMIT

def findPatterns(bulbSet):
    patterns = exponentialPower(2, bulbSet)
    return patterns - 1

if __name__ == '__main__':
    testCases = int(input())
    for _ in range(testCases):
        bulbSet = int(input())
        patterns = findPatterns(bulbSet)
        print(patterns)
