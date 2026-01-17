import sys

input = sys.stdin.readline
n = int(input().rstrip())
supply = list(map(int, input().split()))
supply.sort()
m = int(input().rstrip())
request = list(map(int, input().split()))

def binary_search(data, target, start, end):
    if start > end:
        return 'no'
    mid = (start + end) // 2
    if data[mid] == target:
        return 'yes'
    elif data[mid] < target:
        return binary_search(data, target, mid + 1, end)
    else:
        return binary_search(data, target, start, mid - 1)
    
result = ['no'] * m
for i in range(m):
    result[i] = binary_search(supply, request[i], 0, n - 1)


for i in result:
    print(i, end = ' ')