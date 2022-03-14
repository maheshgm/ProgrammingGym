# Problem Link: https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/practice-problems/algorithm/chef-and-chefa-a5c8800a/

def solve(A, B):
    max_score = 0
    max_energy = sorted(A, reverse=True)
    min_energy = sorted(B)
    for i,j in zip(max_energy, min_energy):

        winner_score = i-j
        max_score += winner_score if winner_score > 0 else 0
    return max_score

if __name__ == '__main__':
    num_levels = int(input())
    bob_levels = list(map(int, input().split()))
    james_levels = list(map(int, input().split()))

    max_score = solve(bob_levels, james_levels)
    print(max_score)