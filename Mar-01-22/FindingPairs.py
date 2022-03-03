# Problem Link: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm
# /find-pairs-4-699bc085/

def DFSUtil(node, visited, graph, edges):
    stack = [node]

    while len(stack) != 0:
        node = stack.pop()
        visited[node] = 1
        for child in graph[node]:
            if visited[child] == 0:
                edges[child] = edges[node] + 1
                stack.append(child)



if __name__ == '__main__':
    N = int(input())
    graph = [[] for i in range(N + 1)]
    edges = [0] * (N*(N-1) // 2)
    for i in range(N - 1):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)
    edges[1] = 1
    visited = [0] * (N + 1)
    DFSUtil(1, visited, graph, edges)

    sumOfEdges = sum(edges)
    print(sumOfEdges)
