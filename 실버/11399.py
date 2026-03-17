# N 명의 사람 1번부터 N번까지 번호가 매겨져 있다. i 번 사람의 돈 인출 시간은 pi 분 
# 걸린다. 모든 사람이 돈을 인출하는데 필요한 최소 시간 구하라
import sys
input = sys.stdin.readline
result = 0
tjs = 0
N = int(input())
p = list(map(int, input().split()))
p = p[: N]
p.sort()
for i in p:
  result += i
  tjs += result

print(tjs)