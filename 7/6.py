n = int(input())
data = [0] * 1000000

for i in input().split():
    data[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if data[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')