# Problem Link: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/approximate/longest-common-increasing-subsequence-c70b9f4a/
def solve(A,N,B,M):
    indices = []
    table = {}
    for i in range(N):
        table[A[i]] = i+1

    for i in range(M):
        if B[i] in table:
            indices.append(table[B[i]])
            indices.append(i+1)
            return indices
    return 0

if __name__ == '__main__':
    N,M = map(int,input().split())
    L = list(map(int,input().split()))
    A = L[:N]
    B = L[N:]

    indices = solve(A,N,B,M)
    if indices == 0:
        print(0)
    else:
        print(1)
        print(indices[0])
        print(indices[1])
