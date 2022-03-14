# Problem Link: https://www.hackerearth.com/problem/algorithm/cemented-strings-8d14b2a2/

def solve(bucket_str):
    uniq_buckets = [0] * 26
    final_cost = 0
    for i in range(len(bucket_str)):
        bucket_num = ord(bucket_str[i]) - ord('a')
        for j in range(bucket_num+1, 26):
            final_cost += uniq_buckets[j]
        final_cost += 1
        uniq_buckets[bucket_num] += 1
    return final_cost


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        str_len = int(input())
        bucket_str = input()
        final_cost = solve(bucket_str)
        print(final_cost)