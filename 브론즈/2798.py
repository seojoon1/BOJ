import sys
input = sys.stdin.readline
a, b = map(int, input().split())
cards = list(map(int, input().split()))
cards = cards[:a]
result = 0
for i in range(a):
  for j in range(i + 1, a):
    for k in range(j + 1, a):
      sum = cards[i] + cards[j] + cards[k]
      if sum <= b:
        result = max(result, sum)
print(result)
