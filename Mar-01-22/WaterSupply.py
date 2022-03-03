# Problem Link : https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/water-flow-4-38cea6c6/

visited = []
graph = []
citiesCount = 0


def DFSUtil(node):
    global  citiesCount, visited, graph, blockedCities
    citiesCount += 1
    if blockedCities[node-1] == 1:
        return
    visited[node] = 1
    for child in graph[node]:
        if visited[child] == 0:
            DFSUtil(child)

def solve(N, edges):
    global visited, graph
    visited = [0]*(N+1)
    graph = [ [] for i in range(N+1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    res = -1
    for i in range(1, N+1):
        if visited[i] == 0:
            global citiesCount
            citiesCount = 0
            DFSUtil(i)
            res = max(res, citiesCount)
    print(res)

if __name__ == '__main__':
    global blockedCities
    N = int(input())
    edges = []
    for i in range(N-1):
        a,b = map(int,input().split())
        edges.append((a,b))
    blockedCities = list(map(int,input().split()))
    solve(N,edges)