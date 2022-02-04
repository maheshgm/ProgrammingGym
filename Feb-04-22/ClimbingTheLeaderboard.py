# Problem Link      : https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
# Difficulty Level  : Medium

def climbingLeaderboard(ranked,playerScores):
    ranked = sorted(list(set(ranked)),reverse=True)
    rankings = []
    for score in playerScores:
        while ranked and score >= ranked[-1]:
            ranked.pop()
        rankings.append(len(ranked)+1)

    return rankings


if __name__ == '__main__':
    noOfPlayers = int(input())
    ranked = list(map(int,input().split()))
    noOfGames = int(input())
    playerScores = list(map(int,input().split()))
    rankings = climbingLeaderboard(ranked,playerScores)
    for rank in rankings:
        print(rank)
