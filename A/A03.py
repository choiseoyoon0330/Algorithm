data = input()

result = 0
cnt0 = 0
cnt1 = 0

prev = None
for i in data:
    if i != prev:
        if i == '0':
            cnt0 += 1
        else:
            cnt1 += 1
        prev = i

print(min(cnt0, cnt1))