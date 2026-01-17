n, x = map(int, input().split())
data = list(map(int, input().split()))

def binary_search_under(data, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or target > data[mid - 1]) and data[mid] == target:
        return mid
    elif data[mid] < target:
        return binary_search_under(data, target, mid + 1, end)
    else:
        return binary_search_under(data, target, start, mid - 1)
        
def binary_search_top(data, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == n - 1 or data[mid + 1] > target) and data[mid] == target:
            return mid
    elif data[mid] < target:
        return binary_search_top(data, target, mid + 1, end)
    else:
        return binary_search_top(data, target, start, mid - 1)

top = binary_search_top(data, x, 0, n - 1)  
under = binary_search_under(data, x, 0, n - 1)

if top == None or under == None:
    print(-1)
else:
    print(top - under + 1)