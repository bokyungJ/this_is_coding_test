# 못품
n,m = map(int, input().split())
graph = [[]for _ in range(n)]

for i in range(n):
    graph[i].append(list(map(int, input().split())))

visited = [0]*(n+1)
print(graph)