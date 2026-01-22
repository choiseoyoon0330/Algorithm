n, m = map(int, input().split())
data = []
array = [10001] * (m + 1)
array[0] = 0

for _ in range(n):
    data.append(int(input()))
data.sort()

for i in data:
    for j in range(i, m + 1):
        if array[j - i] != 10001:
            array[j] = min(array[j], array[j - i] + 1)

result = array[m]
if result == 10001:
    result = -1
print(result)