n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

def selection_sort(data):
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[min_idx] > data[j]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

def insertion_sort(data):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
            else:
                break
    return data

data.sort()
print(*data)
        