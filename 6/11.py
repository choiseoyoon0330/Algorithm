n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    data.append((name, int(score)))

data = sorted(data, key = lambda student: student[1])
for student in data:
    print(student[0], end = ' ')