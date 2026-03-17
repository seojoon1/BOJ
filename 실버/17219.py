#이거 푸키먼 아님?
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memojang = {}
bibun = []
for i in range(1,N+1):
  name, password = input().strip().split()
  memojang[name] = password
for j in range(M):
  q = input().strip()
  bibun.append(memojang[q])
for k in bibun:
  print(k)

