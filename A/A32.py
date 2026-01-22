n = int(input())
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(array[i])):
        if j == 0:
            left_up = 0
        else:
            left_up = array[i - 1][j - 1]
        if j == i:
            right_up = 0
        else:
            right_up = array[i - 1][j]
        
        array[i][j] = array[i][j] + max(left_up, right_up)

result = 0
for i in range(n):
    result = max(array[n - 1][i], result)
print(result)