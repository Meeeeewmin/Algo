#최단경로
import heapq

N_, M = map(int, input().split())
N = N_ + 1
arr = [[] for _ in range(N)]
for _ in range(M):
    s, e, d = map(int, input().split())
    arr[s].append((e,d))

def dajkstra(start):
    distance = [0] * N
    q = []
    heapq.heappush(q, (0, start))
    

    while q:
        dis, s = heapq.heappop(q)

        if dis > distance[s]:
            continue
        
        for node in arr[s]:
            if distance[node[0]] > dis + node[1] or distance[node[0]] == 0:
                distance[node[0]] = dis + node[1]
                heapq.heappush(q, (distance[node[0]], node[0]))

    return distance

result = dajkstra(1)
print(result[N-1])