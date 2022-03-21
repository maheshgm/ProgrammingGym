# Problem Link: https://www.codechef.com/START30D/problems/SWAPCW

def solve(inp_str, str_len):
    srt_str = list(sorted(inp_str))

    for i in range(str_len):
        if inp_str[i] != srt_str[i]:
            srt_str[i], srt_str[str_len-1-i] = srt_str[str_len-1-i], srt_str[i]

    return "".join(srt_str) == inp_str

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        str_len = int(input())
        inp_str = input()
        res_val = solve(inp_str, str_len)

        if res_val:
            print("YES")
        else:
            print("NO")