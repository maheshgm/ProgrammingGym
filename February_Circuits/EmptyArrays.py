# Problem Link: https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/algorithm/empty-array-31ed638c/

def solve(first, second):
    count = 0

    while len(first) != 0:
        if first[0] == second[0]:
            first.pop(0)
            second.pop(0)
        else:
            temp = first[0]
            first.pop(0)
            first = first + [temp]

        count += 1

    return count

if __name__ == '__main__':
    test_cases = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    result = solve(A,B)
    print(result)