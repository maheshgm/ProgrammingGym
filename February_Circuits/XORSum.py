# Problem Link : https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/xor-split-2-46b24557/

def solve(N):
    if N == 0 or (N&N-1) == 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        N = int(input())
        result = solve(N)
        print(result)