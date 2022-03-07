# Problem Link : https://www.hackerearth.com/practice/codemonk/

top_down_dp_table = {}

def solve(N):
    top_down_dp_table[0] = 1
    top_down_dp_table[1] = 10
    if N in top_down_dp_table:
        return top_down_dp_table[N]

    left_sub = solve(N//2)
    right_sub = solve(N//2 - 1)
    if (N & 1) == 0:
        top_down_dp_table[N] = (left_sub**2 - right_sub**2) % 1000000009
    else:
        last_sub = solve(N//2 + 1)
        top_down_dp_table[N] = (left_sub * (last_sub - right_sub)) % 1000000009

    return top_down_dp_table[N]
if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        N = int(input())
        result = solve(N)
        print(result)
        top_down_dp_table.clear()