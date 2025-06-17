n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
players = list(range(n))
min_diff = float('inf')

def comb(arr, r):
    if r == 0:
        return [[]]
    result = []
    for i in range(len(arr)):
        for rest in comb(arr[i+1:], r-1):
            result.append([arr[i]] + rest)
    return result

teams = comb(players, n // 2)

while teams:
    team1 = teams.pop(0)
    team2 = teams.pop()
    score1 = score2 = 0
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            score1 += board[team1[i]][team1[j]] + board[team1[j]][team1[i]]
            score2 += board[team2[i]][team2[j]] + board[team2[j]][team2[i]]
    min_diff = min(min_diff, abs(score1 - score2))

print(min_diff)
