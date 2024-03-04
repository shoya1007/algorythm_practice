N, S = map(int, input().split())
sum = 0
for r in range(1, N + 1):
    for b in range (1, N + 1):
        if r + b <= S:
            sum += 1
print(sum)
