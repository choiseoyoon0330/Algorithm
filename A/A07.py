import sys
input = sys.stdin.readline

n = input()
k = len(n)
result = 0

for i in range(k // 2):
    result += int(n[i])
for j in range(k //2, k - 1):
    result -= int(n[j])

if result == 0:
    print('LUCKY')
else:
    print('READY')