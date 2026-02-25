import sys
input = sys.stdin.readline
N = int(input())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
print(dp[N])

#이전 것을 참고해야하는 문제 - 1을 빼는 경우, 2로 나누는 경우, 3으로 나누는 경우를 모두 고려해서 dp 배열에 저장해야함