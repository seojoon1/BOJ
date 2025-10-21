h, m = map(int, input().split())
oh = int(input())
if m + oh >= 60:
    h += int((m + oh) / 60)
    m = (m + oh) % 60
    if h >= 24:
        h = h % 24
else:
    m += oh
print(h, m)