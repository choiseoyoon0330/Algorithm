n, m = map(int, input().split())
data = list(map(int, input().split()))
max_val = max(data)

def binary_search(array, target, start, end):
    if start > end:
        return min(start, end)
    mid = (start + end) // 2
    total = 0
    for i in range(n):
        if array[i] > mid:
            total += array[i] - mid
    if total > target:
        return binary_search(array, target, mid + 1, end)
    elif total == target:
        return mid
    else:
        return binary_search(array, target, start, mid - 1)
        
    
print(binary_search(data, m, 0, max_val))