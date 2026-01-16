# count sort
data = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
max_val = max(data)
min_val = min(data)
array = [0] * (max_val - min_val + 1)

for i in range(len(data)):
    array[data[i]] += 1

for i in range(len(array)):
    for j in range(array[i]):
        print(i, end = ' ')

