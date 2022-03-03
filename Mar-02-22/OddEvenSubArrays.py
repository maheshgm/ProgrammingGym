# Problem Link : https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/odd-even-subarrays-72ad69db/

def reduceNum(num):
    if num & 1 == 1:
        return -1
    else:
        return 1


def findOddEvenSubArrays(Array, N):
    transFormedArray = list(map(reduceNum, Array))
    # print(transFormedArray)

    prefixSum = [0]
    t = 0
    for i in range(N):
        prefixSum.append(prefixSum[-1] + transFormedArray[i])
    counter = dict()
    result = 0

    for s in prefixSum:
        if s in counter:
            result += counter[s]
            counter[s] += 1
        else:
            counter[s] = 1
    return result


if __name__ == '__main__':
    N = int(input())
    Array = list(map(int, input().split()))
    result = findOddEvenSubArrays(Array, N)
    print(result)
