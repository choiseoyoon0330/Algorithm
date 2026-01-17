import heapq

n = int(input())
pq = []
for _ in range(n):
    heapq.heappush(pq, (int(input())))
    
result = 0

while len(pq) > 1:
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    add = a + b
    result += add
    heapq.heappush(pq, add)
        
print(result)