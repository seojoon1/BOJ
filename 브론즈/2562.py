num_list = []
for _ in range(9):
    num = int(input())
    num_list.append(num)
result = max(num_list)
print(result)
print(num_list.index(result)+1)