import sys
input = sys.stdin.readline
N = int(input())
num = 666
count = 0
while True:
  if '666' in str(num): #N 번쨰 666이 포함된 영화를 찾는거니까 666 이 나올 때마다 카운트를 증가시킴 만약 카운트가 N이 되면 그 때의 num이 답이 됨
    count += 1
  if count == N:
    print(num)
    break
  num += 1