import sys
input = sys.stdin.readline
N = int(input())
cut = int(N * 0.15 + 0.5)
ar = []
for i in range(N):
  ar.append(int(input().strip()))
arSort = sorted(ar)
arSort = arSort[cut:-cut] if cut > 0 else arSort
try:
  if N > 3:
    print(int(sum(arSort) / len(arSort) + 0.5))
  else:
    print(int(sum(ar) / N + 0.5))
except ZeroDivisionError:
  print(0)