def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid + 1
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)

n, target = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = binary_search(data, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result)