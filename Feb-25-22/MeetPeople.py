# Problem Link: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/emergency-meeting-da1fc0b5/
'''
    The algorithm used is based on the Breadth First Search Traversal algorithm.
'''


def findMinTime(N, K, edges, people):
    graph = [[] for i in range(N + 1)]
    level = [0] * (N + 1)
    isPeople = [0] * (N + 1)

    for edge in edges:
        graph[edge[0]].append(edge[1])
    for p in people:
        isPeople[p] = 1

    visited = [0] * (N + 1)
    visited[1] = 1

    Q = [1]
    while len(Q) != 0:
        neighbour = Q[0]
        Q.pop(0)

        for vertex in graph[neighbour]:
            if visited[vertex] == 0:
                visited[vertex] = 1
                Q.append(vertex)
                level[vertex] = level[neighbour] + 1
                level[vertex] %= 2
    for p in range(1, K):
        if level[people[p]] != level[people[p - 1]]:
            return -1
    distance = [0] * (N + 1)
    visited = [0] * (N + 1)
    visited[1] = 1
    maxV = 1
    Q=[people[0]]

    while len(Q) != 0:
        v = Q[0]
        Q.pop(0)
        if isPeople[v]:
            maxV = v
        for u in graph[v]:
            if visited[v] == 0:
                visited[u] = 1
                Q.append(u)
                distance[u] = distance[v] + 1

    res = distance[maxV] // 2
    visited = [0] * (N + 1)
    distance = [0] * (N + 1)

    visited[maxV] = 1
    Q = [maxV]
    while len(Q) != 0:
        v = Q[0]
        Q.pop(0)

        if isPeople[v] == 1:
            res = max(res, distance[v] // 2)
        for u in graph[v]:
            if visited[u] == 0:
                visited[u] = 1
                Q.append(u)
                distance[u] = distance[v] + 1

    return res


if __name__ == '__main__':
    testCases = int(input())
    for _ in range(testCases):
        N, K = map(int, input().split())
        edges = []
        people = []
        for i in range(N - 1):
            start, end = map(int, input().split())
            edges.append((start, end))
        people = list(map(int, input().split()))

        result = findMinTime(N, K, edges, people)
        print(result)
