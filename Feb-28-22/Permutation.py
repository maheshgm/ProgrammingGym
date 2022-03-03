# Problem Link: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems
# /algorithm/t1-1-6064aa64/

def solve(seq, N):
    sortedSeq = "".join(sorted(seq))

    Q = [seq]
    visited = dict()
    visited[seq] = 1

    while len(Q) != 0:
        t = Q[0]
        Q.pop(0)
        if t == sortedSeq:
            break
        for i in range(2, len(t) + 1):
            rev = t[:i][::-1] + t[i:]
            if rev not in visited:
                visited[rev] = visited[t] + 1
                Q.append(rev)
    # print(visited)
    print(visited[sortedSeq] - 1)


if __name__ == '__main__':
    N = int(input())
    seq = "".join(input().split())
    solve(seq, N)
