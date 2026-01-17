n = int(input())
data = set(map(int, input().split()))

m = int(input())
request = list(map(int, input().split()))

for i in request:
    if i in data:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')