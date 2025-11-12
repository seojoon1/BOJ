import sys
from collections import deque #양방향 큐 사용
n = int(sys.stdin.readline())
ar = deque()
for i in range(n):
    ar.append(i+1)
while len(ar) > 1:
    ar.popleft()
    ar.append(ar.popleft())
print(ar[0])