n = int(input())
score = list(map(int, input().split()))
score = score[:n]
max_score = max(score)
new_score = []
for i in score:
    new_score.append(i / max_score * 100)
min_score = sum(new_score)/n
print(min_score)