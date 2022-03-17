# Problem Link : https://www.codechef.com/START30C/problems/CHEFBOTTLE

def solve(N,X,K):
    max_bottles = N
    bottles_filled = K // X
    max_bottles = min(bottles_filled, max_bottles)

    return max_bottles

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        N,X,K = map(int,input().split())
        max_bottles = solve(N,X,K)
        print(max_bottles)