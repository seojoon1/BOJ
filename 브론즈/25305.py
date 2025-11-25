import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a = a[:n]
a.sort(reverse=True)
a = a[:k]
print(a[-1])