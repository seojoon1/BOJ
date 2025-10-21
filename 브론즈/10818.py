n = int(input())
num = list(map(int, input().split()))
num = num[:n]
print(min(num), max(num))