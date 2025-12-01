import sys
input = sys.stdin.readline

n = int(input())
numbers = int(input())
numbers_list = list(map(int, str(numbers)))
numbers_list = numbers_list[:n]
print(sum(numbers_list))