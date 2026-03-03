import sys
input = sys.stdin.readline
N, M = map(int, input().split())
a = {}
b = {}
for i in range(1,N+1):
  name = input().strip()
  a[name] = i
  b[i] = name
for j in range(M):
  q = input().strip()
  
  if q.isdigit():
    print(b[int(q)])
  else:
    print(a[q])
#리스트는 시간초과 뜸 그래서 딕셔너리로 바꿈
