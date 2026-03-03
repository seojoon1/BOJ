import sys
input = sys.stdin.readline
M = int(input())
s = set()
for _ in range(M):
  data = input().split()
  N = data[0]
  if len(data) == 2:
    X = int(data[1])
  if N == 'add':
    s.add(X)
  elif N == 'remove':
    s.discard(X)
  elif N == 'check':
    if X in s:
      print(1)
    else:
      print(0)
  elif N == 'toggle':
    if X in s:
      s.discard(X)
    else:
      s.add(X)
  elif N == 'all':
    s = set(i for i in range(1, 21))
  elif N == 'empty':
    s.clear()