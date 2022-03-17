# Problem Link: https://www.codechef.com/START30C/problems/BALREV
def solve(bin_s, len_s):
    str_l = list(bin_s)
    for i in range(len_s-1):
        for j in range(len_s-i-1):
            if str_l[j] > str_l[j+1]:
                str_l[j], str_l[j+1] = str_l[j+1], str_l[j]

    result = "".join(str_l)
    return result


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        length = int(input())
        bin_str = input()

        result = solve(bin_str, length)

        print(result)