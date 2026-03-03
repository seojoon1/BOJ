#듣보잡
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
name = set()
see = set()
for i in range(N):
  name.add(input().strip())
for j in range(M):
  see.add(input().strip())
dbj = name & see
dbj = list(dbj)
dbj.sort()
print(len(dbj))
for m in dbj:
  sys.stdout.write(m+'\n')
#set으로 교집합 구하기