n, k = map(int, input().split())
cnt = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            clock = f"{h:02d}{m:02d}{s:02d}"
            cnt += str(k) in clock
print(cnt)