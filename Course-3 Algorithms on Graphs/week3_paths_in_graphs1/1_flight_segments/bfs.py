#Uses python3

import sys
from collections import deque
from sys import maxsize

def distance(adj, s, t):
    dist = [maxsize for _ in range(len(adj))]
    dist[s] = 0
    vertex_queue = deque()
    vertex_queue.append(s)
    while len(vertex_queue) != 0:
        cur_source = vertex_queue.popleft()
        for vertex in adj[cur_source]:
            if dist[vertex] == maxsize:
                vertex_queue.append(vertex)
                dist[vertex] = dist[cur_source] + 1
    return dist[t] if dist[t] != maxsize else -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
