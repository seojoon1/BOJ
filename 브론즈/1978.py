import sys
input = sys.stdin.readline
N = int(input())
pc = 0
a = list(map(int, input().split()))
a = a[:N]
for i in a:
  if i > 1:
    for j in range(2, i):
      if i % j == 0:
        break
    else:
      pc += 1
print(pc)

