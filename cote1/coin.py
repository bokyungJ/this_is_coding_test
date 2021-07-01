n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

temp = [[0]*m for _ in range(n)]
temp[0][0] = graph[0][0]

result = graph[n-1][m-1]

dx = [0,1,1]
dy = [1,0,1]

def dfs(x,y):
    global result
    for i in range(3):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            temp[nx][ny] = temp[x][y]+graph[nx][ny]
            dfs(nx,ny)
            result = max(result, temp[n-1][m-1])
            temp[nx][ny] = graph[nx][ny]
    return result

print(dfs(0,0))

'''
오른쪽,아래,대각선만 이동 가능
제일 동전 많이 줍기
input 예시
3 4
1 2 3 4
0 0 0 5
6 7 8 9
'''
