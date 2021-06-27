from collections import deque

# bfs 함수 정의
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    # queue가 빌때까지 반복
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

# graph 정의
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 방문처리
visited = [False]*9

bfs(graph, 1, visited)