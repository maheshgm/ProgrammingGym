# Problem Link:

def solve(currentKeyValue, finalKey, N, keys):

    Q = [currentKeyValue]
    visited = dict()
    visited[currentKeyValue] = 0
    while len(Q) != 0:
        k = Q.pop(0)
        if k == finalKey:
            break
        for availKey in keys:
            resKey = (k * availKey) % 100000
            if resKey not in visited:
                visited[resKey] = visited[k] + 1
                Q.append(resKey)
    if finalKey not in visited:
        print(-1)
    else:
        print(visited[finalKey])


if __name__ == '__main__':
    currentKeyValue, finalKey = map(int,input().split())
    N = int(input())
    keys = list(map(int,input().split()))
    solve(currentKeyValue, finalKey, N, keys)