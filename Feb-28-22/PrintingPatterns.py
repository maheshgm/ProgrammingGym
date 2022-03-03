# Problem Link : https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/waves-b18625d7/

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def solve(A,B,C,D):
    res = [[0]*1000 for i in range(1000) ]
    visited = [[0]*1000 for i in range(1000) ]
    Q = [(C,D)]
    visited[C][D] = 1

    while len(Q) != 0:
        cx,cy = Q[0][0], Q[0][1]
        Q.pop(0)

        for i in range(8):
            x = cx + dx[i]
            y = cy + dy[i]
            if (x<0 or x>A or y<0 or y>B) or visited[x][y] == 1:
                continue
            else:
                res[x][y] = res[cx][cy] + 1
                visited[x][y] = 1
                Q.append((x,y))
    for i in range(A):
        for j in range(B):
            print(res[i][j], end = " ")
        print()



if __name__ == '__main__':
    A,B,C,D = map(int,input().split())
    solve(A,B,C,D)
