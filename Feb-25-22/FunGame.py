# Problem Link: https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/fun-game-91510e9f/

arrayLength = int(input())
array = list(map(int,input().split()))

start = 0
end = arrayLength-1

while start != arrayLength and end != -1:
    if array[start] > array[end]:
        print("1", end=" ")
        end -= 1
    elif array[start] < array[end]:
        print("2", end=" ")
        start += 1
    else:
        print("0", end=" ")
        start += 1
        end -= 1
