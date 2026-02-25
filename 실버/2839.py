#1 적게 가져가기 == 5로 나눠보기 나눠떨어지면 그게 답 (봉지의 개수)
#2 5로 나눠떨어지지 않으면 3씩 빼면서 5로 나눠지는지 확인하기(3씩 빼는 횟수는 봉지의 개수)
#3 5로 나눠떨어지는 경우가 나오면 그때까지 3씩 빼는 횟수 + 5로 나눠떨어지는 몫이 답
#4 계속 안 나와서 N이 음수가 되면 -1 출력하기
import sys
input = sys.stdin.readline
bong = 0
N = int(input())
while True:
  if N < 0:
    bong = -1
    break
  if N % 5 == 0:
    bong += N // 5
    break
  elif N % 5 != 0:
    N -= 3
    bong += 1
    continue
print(bong)