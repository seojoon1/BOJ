import sys
input = sys.stdin.readline
max_num = 10000
count = [0] * (max_num + 1)
N = int(input())
for _ in range(N):
    num = int(input())
    count[num] += 1
for i in range(max_num + 1):
    if count[i] != 0:
        for _ in range(count[i]):
            sys.stdout.write(f"{i}\n")
