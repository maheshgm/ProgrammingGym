# Problem Link: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/manhattan-2fc15b93/

def computeDistance(X, Y):
    sumOfX = sum(X)
    sumOfY = sum(Y)
    N = len(X)
    X.sort()
    Y.sort()

    current_x, current_y, res =0, 0, 0
    for i in range(N-1):
        res += (sumOfX - (N-i)* X[i]) - current_x
        res += (sumOfY - (N-i)* Y[i]) - current_y

        current_x += X[i]
        current_y += Y[i]
    return res

if __name__ == '__main__':
    testCases = int(input())
    for _ in range(testCases):
        N = int(input())
        X = []
        Y = []
        for i in range(N):
            x,y = map(int,input().split())
            X.append(x)
            Y.append(y)
        res = computeDistance(X,Y)
        print(res)
