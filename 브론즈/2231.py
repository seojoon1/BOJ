# 자연수 N의 생성자를 구하는 문제
# 분해합 은 N과 N의 각 자리수를 더한 값
# 분해합 - N의 자리수*자리의 최대수인 9 = 생성자보다 작은 수
import sys
input = sys.stdin.readline
N_str = input().strip()
result = 0
N = int(N_str)
start = max(1, N - len(N_str) * 9)
for i in range (start, N):
  bhh = i + sum(map(int, str(i))) #생성자 보다 작은 수에서 N 까지의 수 중에 분해합이 N과 같다면 그 수가 생성자
  if bhh == N:
    result = i
    break
print(result)

