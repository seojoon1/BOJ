list = []
while True:
    try:
        a, b, c = map(int, input().split())
        if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
            list.append("right")
        else:
            list.append("wrong")
    except:
        break
for i in range(len(list)-1):
    print(list[i])
