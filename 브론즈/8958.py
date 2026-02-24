import sys
input = sys.stdin.readline
N = int(input())
a = []
for _ in range(N):
  x = input().rstrip()
  ts = 0
  p = 1
  for j in x:
    if j == "O":
      ts += p
      p += 1
    else:
      p = 1
  a.append(ts)
print('\n'.join(map(str,a)))

